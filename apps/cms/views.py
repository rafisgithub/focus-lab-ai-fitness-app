from rest_framework.views import APIView
from rest_framework.response import Response

from django.utils import translation
from .serializers import (
    BrandSerializer,
    FeatureSerializer,
    TestimonialSerializer,
    BenefitSerializer,
    FaqSerializer,
    PageSerializer,
    HeroSectionSerializer,
    HowItWorkSerializer,
    InterviewCoachSectionSerializer,
    FooterSerializer,
    GlobalCtaSerializer,
)
from .models import (
    Brand,
    Feature,
    Footer,
    HeroSection,
    InterviewCoachSection,
    Page,
    Testimonial,
    Benefit,
    Faq,
    HowItWork,
    UpcomingFeatureInterestedUser,
    GlobalCta,
)
from apps.utils.helpers import success, error

# Create your views here.


class BrandAPIView(APIView):

    permission_classes = []

    def get(self, request):
        try:
            lang_code = request.GET.get("lan", "de")
            # print(lang_code)
            translation.activate(lang_code)

            brands = Brand.objects.all()
            serializer = BrandSerializer(brands, many=True)
            return success(
                data=serializer.data, message="Brand list fetched successfully"
            )
        except Exception as e:
            return error(message="Failed to fetch brand list", errors=str(e))


class FeatureAPIView(APIView):
    permission_classes = []

    def get(self, request):
        try:
            lang_code = request.GET.get("lan", "de")
            translation.activate(lang_code)
            features = Feature.objects.all()
            serializer = FeatureSerializer(features, many=True)
            return success(
                data=serializer.data, message="Feature list fetched successfully"
            )
        except Exception as e:
            return error(message="Failed to fetch feature list", errors=str(e))


class TestimonialAPIView(APIView):
    permission_classes = []

    def get(self, request):
        try:
            lang_code = request.GET.get("lan", "de")
            translation.activate(lang_code)
            testimonials = Testimonial.objects.all()
            serializer = TestimonialSerializer(testimonials, many=True)
            return success(
                data=serializer.data, message="Testimonial list fetched successfully"
            )
        except Exception as e:
            return error(message="Failed to fetch testimonial list", errors=str(e))


class BenefitAPIView(APIView):
    permission_classes = []

    def get(self, request):
        try:
            lang_code = request.GET.get("lan", "de")
            translation.activate(lang_code)
            benefits = Benefit.objects.all()
            serializer = BenefitSerializer(benefits, many=True)
            return success(
                data=serializer.data, message="Benefit list fetched successfully"
            )
        except Exception as e:
            return error(message="Failed to fetch benefit list", errors=str(e))


class FaqAPIView(APIView):
    permission_classes = []

    def get(self, request):
        try:
            lang_code = request.GET.get("lan", "de")
            translation.activate(lang_code)
            faqs = Faq.objects.filter(is_active=True)
            serializer = FaqSerializer(faqs, many=True)
            return success(
                data=serializer.data, message="FAQ list fetched successfully"
            )
        except Exception as e:
            return error(message="Failed to fetch FAQ list", errors=str(e))


class PagesAPIView(APIView):
    permission_classes = []

    def get(self, request):
        try:
            # lang_code = request.GET.get('lan', 'de')
            # get language code from headers
            # print(lang_code)
            # get type from query params
            lang_code = request.headers.get("Accept-Language", "de").split(",")[0]
            print(lang_code)
            type = request.GET.get("type", None)
            translation.activate(lang_code)

            page = Page.objects.filter(is_active=True, type=type).first()

            print(page)

            serializer = PageSerializer(page)

            return success(
                data=serializer.data, message="Page list fetched successfully"
            )
        except Exception as e:
            return error(message="Failed to fetch page list", errors=str(e))


class HeroSectionAPIView(APIView):
    permission_classes = []

    def get(self, request):
        try:
            lang_code = request.GET.get("lan", "de")
            translation.activate(lang_code)
            hero_section = HeroSection.objects.first()
            serializer = HeroSectionSerializer(hero_section)
            return success(
                data=serializer.data, message="Hero section fetched successfully"
            )
        except Exception as e:
            return error(message="Failed to fetch hero section", errors=str(e))


class HowItWorkAPIView(APIView):
    permission_classes = []

    def get(self, request):
        try:
            lang_code = request.GET.get("lan", "de")
            print(lang_code)
            translation.activate(lang_code)
            how_it_works = HowItWork.objects.all()
            serializer = HowItWorkSerializer(how_it_works, many=True)
            return success(
                data=serializer.data, message="How It Works list fetched successfully"
            )
        except Exception as e:
            return error(message="Failed to fetch How It Works list", errors=str(e))


class InterviewCoachSectionAPIView(APIView):
    permission_classes = []

    def get(self, request):
        try:
            lang_code = request.GET.get("lan", "de")
            translation.activate(lang_code)
            interview_coach_section = InterviewCoachSection.objects.first()
            serializer = InterviewCoachSectionSerializer(interview_coach_section)
            return success(
                data=serializer.data,
                message="Interview Coach Section fetched successfully",
            )
        except Exception as e:
            return error(
                message="Failed to fetch Interview Coach Section", errors=str(e)
            )


class FooterSectionAPIView(APIView):
    permission_classes = []

    def get(self, request):
        try:
            lang_code = request.GET.get("lan", "de")
            translation.activate(lang_code)
            footer_section = Footer.objects.first()
            serializer = FooterSerializer(footer_section)
            return success(
                data=serializer.data, message="Footer Section fetched successfully"
            )
        except Exception as e:
            return error(message="Failed to fetch Footer Section", errors=str(e))


class NotifyMeAPIView(APIView):
    permission_classes = []

    def post(self, request):
        try:
            email = request.data.get("email")
            if not email:
                return error(
                    message="Email is required", errors="Email field cannot be empty"
                )
            if UpcomingFeatureInterestedUser.objects.filter(email=email).exists():
                return error(
                    message="Email already exists",
                    errors="This email is already registered for notifications",
                )

            user = UpcomingFeatureInterestedUser.objects.create(email=email)
            return success(
                {"email": user.email},
                message="Thanks for your interest! You will be notified when the feature is available.",
            )
        except Exception as e:
            return error(message="Failed to send notification", errors=str(e))


class GlobalCtaAPIView(APIView):
    permission_classes = []

    def get(self, request):
        try:
            lang_code = request.GET.get("lan", "de")
            translation.activate(lang_code)
            global_cta = GlobalCta.objects.first()
            if not global_cta:
                return error(
                   [], message="Global CTA not found", errors="No Global CTA available"
                )
            serializer = GlobalCtaSerializer(global_cta)
            return success(
                data=serializer.data, message="Global CTA fetched successfully"
            )
        except Exception as e:
            return error(message="Failed to fetch Global CTA", errors=str(e))
