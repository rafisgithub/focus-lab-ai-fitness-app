from django.urls import path
from .views import (
    OnboardingView
)

urlpatterns = [
    path("onboarding/", OnboardingView.as_view(), name="onboarding"),

]