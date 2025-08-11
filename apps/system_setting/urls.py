from django.urls import path

from .views import (
    AboutSystemAPIView,
)

urlpatterns = [
    path("about-system/", AboutSystemAPIView.as_view(), name="about_system"),
]
