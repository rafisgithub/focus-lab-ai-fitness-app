from django.urls import path

from django.conf.urls.static import static
from project import settings


from .views import (
    AboutSystemAPIView,
    PageAPIView
)

urlpatterns = [
    path("about-system/", AboutSystemAPIView.as_view(), name="about_system"),
    path("pages/", PageAPIView.as_view(), name="pages"),
]
