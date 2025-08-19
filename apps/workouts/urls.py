from django.urls import path

from django.conf.urls.static import static


from .views import (
   WorkoutAPIView,
   UploadBodyImageAPIView,
   CategoryAPIView,
   SearchWorkoutAPIView,
   SuggestedWorkoutAPIView
)

urlpatterns = [
    path("workouts/", WorkoutAPIView.as_view(), name="workouts"),
    path("suggested-workouts/", SuggestedWorkoutAPIView.as_view(), name="suggested-workouts"),
    path("categories/", CategoryAPIView.as_view(), name="categories"),
    path("search-workout/", SearchWorkoutAPIView.as_view(), name="search-workout"),
    path("upload-body-image/", UploadBodyImageAPIView.as_view(), name="upload-body-image")
]
