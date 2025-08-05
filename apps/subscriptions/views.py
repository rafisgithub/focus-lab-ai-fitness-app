from asyncio.log import logger
from datetime import timedelta
import os
from rest_framework.views import APIView
from rest_framework.response import Response
import stripe

from apps.users.models import User
from project import settings
from django.http import HttpResponse
from .serializers import SubscriptionPackageSerializer, CurrentSubscriptionSerializer
from .models import IncomeReport, Package, Subscription
from apps.utils.helpers import success, error
from django.utils import translation
from django.utils.timezone import now
from rest_framework.permissions import IsAuthenticated

class SubscriptionPackageAPIView(APIView):

    permission_classes = []

    def get(self, request):
        try:
            lang_code = request.GET.get('lan', 'de')  
            translation.activate(lang_code)
            packages = Package.objects.all()
            serializer = SubscriptionPackageSerializer(packages, many=True)
            
            return success(serializer.data, message="Package list fetched successfully")
        except Exception as e:
            return error([],"Failed to fetch package list", errors=str(e))
        


class StripeCheckoutAPIView(APIView):
    permission_classes = [IsAuthenticated] 

    def post(self, request):
        price_id = request.data.get('price_id')
        success_url = request.data.get('success_url')
        cancel_url = request.data.get('cancel_url')
        type = request.data.get("type") 
 

        if type not in ["month", "pay_per_download"]:
            return error(message="Invalid type. Must be 'month' or 'pay_per_download'")

        if not price_id or not success_url or not cancel_url:
            return error(message="Missing required parameters", errors="price_id, success_url, and cancel_url are required")

        try:
            mode = 'payment' if type == "pay_per_download" else 'subscription'

            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                customer_email=request.user.email if request.user.is_authenticated else None,
                
                line_items=[{
                    'price': price_id,
                    'quantity': 1,
                }],
                mode=mode,
                success_url=success_url,
                cancel_url=cancel_url,
            )

            return success(checkout_session.url, message="Stripe checkout initiated successfully")
        except Exception as e:
            return error(message="Failed to initiate Stripe checkout", errors=str(e))


class StripeWebhookAPIView(APIView):
    permission_classes = [] 

    def post(self, request):
        payload = request.body
        sig_header = request.META.get('HTTP_STRIPE_SIGNATURE')
        endpoint_secret = os.getenv('STRIPE_WEBHOOK_SECRET', '')

        try:
            event = stripe.Webhook.construct_event(payload, sig_header, endpoint_secret)
        except ValueError as e:
            logger.error("Invalid payload: %s", str(e))
            return HttpResponse(status=400)
        except stripe.error.SignatureVerificationError as e:
            logger.error("Invalid signature: %s", str(e))
            return HttpResponse(status=400)

        try:
            if event['type'] == 'checkout.session.completed':
                session = event['data']['object']
                session_id = session.get('id')
                checkout_session = stripe.checkout.Session.retrieve(
                    session_id,
                    expand=['line_items']
                )

                customer_email = session.get('customer_email')
                user = User.objects.filter(email=customer_email).first()
                if not user:
                    return HttpResponse(status=200)

                line_items = checkout_session['line_items']['data']
                price_id = line_items[0]['price']['id'] if line_items else None
                print("Price ID:", price_id)
                package = Package.objects.filter(stripe_price_id=price_id).first()
                print("Package:", package)
                if not package:
                    return HttpResponse(status=200)

                if package.type == Package.PackageType.PAY_PER_DOWNLOAD:

                    if not Subscription.objects.filter(user=user).exists():
                        Subscription.objects.create(
                            user=user,
                        )
                    subscription = Subscription.objects.filter(user=user).first()
                    print("Subscription:", subscription)
                    if subscription:
                        subscription.pay_per_download_credits += 1
                        subscription.save()
                else:
                    print(Subscription.objects.filter(user=user).first())
                    if(not Subscription.objects.filter(user=user).exists()):
                        Subscription.objects.create(
                            user=user,
                            package=package,
                            stripe_subscription_id=session.get('subscription'),
                            status='active',
                            start_date=now(),
                            end_date=now() + timedelta(days=30),
                        )
                    else:   
                        subscription = Subscription.objects.get(user=user)
                        subscription.package = package
                        subscription.stripe_subscription_id = session.get('subscription')
                        subscription.status = 'active'
                        subscription.start_date = now()
                        subscription.end_date = now() + timedelta(days=30)
                        subscription.save()



                # IncomeReport.objects.update(
                #     total_income=IncomeReport.objects.first().total_income + package.price,
                # )

        except Exception as e:
            logger.exception("Error handling Stripe webhook event: %s", str(e))
            return HttpResponse(status=500)

        return HttpResponse(status=200)  # Always return a response


class AccessStatusAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        try:
            subscription = Subscription.objects.filter(user=user).first()
            print("Subscription:", subscription)
            if subscription:
                has_subscription = subscription.has_subscription()
                print("Has Subscription:", has_subscription)
                has_pay_per_download_credits = subscription.has_pay_per_download_credits()
                print("Has Pay Per Download Credits:", has_pay_per_download_credits)
                return success(
                    data={
                        "has_subscription": has_subscription,
                        "has_pay_per_download_credits": has_pay_per_download_credits
                    },
                    message="Access status checked successfully"
                )
        except Exception as e:
            return error(message="Failed to check access status", errors=str(e))
              


class CurrentSubscriptionPlanAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        try:
            subscription = Subscription.objects.filter(user=user).first()
            if subscription:
                serializer = CurrentSubscriptionSerializer(subscription)
                return success(serializer.data, message="Current subscription plan fetched successfully")
        except Exception as e:
            return error(message="Failed to fetch current subscription plan", errors=str(e))
          