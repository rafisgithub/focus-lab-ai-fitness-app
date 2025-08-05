from django.conf import settings
from django.urls import path

from apps.cms.models import Feature

from .views import ContactUsAPIView

urlpatterns = [
    path("contact-us/", ContactUsAPIView.as_view(), name="contact_us"),
]
