from django.conf import settings
from django.urls import path


from .views import (
    SubscriptionPackageAPIView,
    StripeCheckoutAPIView,
    StripeWebhookAPIView,
    AccessStatusAPIView,
    CurrentSubscriptionPlanAPIView,
)

urlpatterns = [
    path("subscription-packages/", SubscriptionPackageAPIView.as_view(), name="subscription_packages_list"),
    path("stripe-checkout/", StripeCheckoutAPIView.as_view(), name="stripe_checkout"),
    path("stripe-webhook/", StripeWebhookAPIView.as_view(), name="stripe_webhook"),
    path("access-status/", AccessStatusAPIView.as_view(), name="access_status"),
    path("current-subscription-plan/", CurrentSubscriptionPlanAPIView.as_view(), name="current_subscription_plan"),
]
