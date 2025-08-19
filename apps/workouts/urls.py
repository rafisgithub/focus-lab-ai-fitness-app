from django.urls import path

from django.conf.urls.static import static


from .views import (
   WorkoutAPIView,
   UploadBodyImageAPIView,
   CategoryAPIView
)

urlpatterns = [
    path("workouts/", WorkoutAPIView.as_view(), name="workouts"),
    path("categories/", CategoryAPIView.as_view(), name="categories"),
    path("upload-body-image/", UploadBodyImageAPIView.as_view(), name="upload-body-image")
]
