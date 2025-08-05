from django.conf import settings
from django.urls import path

from apps.cms.models import Feature

from .views import (
    BrandAPIView,
    FeatureAPIView,
    TestimonialAPIView,
    BenefitAPIView,
    FaqAPIView,
    PagesAPIView,
    HeroSectionAPIView,
    HowItWorkAPIView,
    InterviewCoachSectionAPIView,
    FooterSectionAPIView,
    NotifyMeAPIView,
    GlobalCtaAPIView,
)

urlpatterns = [
    path("hero-section/", HeroSectionAPIView.as_view(), name="hero_section"),
    path("brands/", BrandAPIView.as_view(), name="brands_list"),
    path("features/", FeatureAPIView.as_view(), name="features_list"),
    path("testimonials/", TestimonialAPIView.as_view(), name="testimonials_list"),
    path("benefits/", BenefitAPIView.as_view(), name="benefits_list"),
    path("faqs/", FaqAPIView.as_view(), name="faqs_list"),
    path("pages/", PagesAPIView.as_view(), name="pages_list"),
    path("how-it-works/", HowItWorkAPIView.as_view(), name="how_it_works_list"),
    path(
        "interview-coach-section/",
        InterviewCoachSectionAPIView.as_view(),
        name="interview_coach_section",
    ),
    path("footer-section/", FooterSectionAPIView.as_view(), name="footer_section"),
    path("notify-me/", NotifyMeAPIView.as_view(), name="notify_me"),
    path("global-cta/", GlobalCtaAPIView.as_view(), name="global_cta"),
]
