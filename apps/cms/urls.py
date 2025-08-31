from django.urls import path
from .views import (
   PageApiView
)

urlpatterns = [
    path("pages/", PageApiView.as_view(), name="page-list"),

]