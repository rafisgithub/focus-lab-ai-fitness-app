from django.urls import path

from django.conf.urls.static import static


from .views import (
   WorkoutAPIView,
   UploadBodyImageAPIView,
   CategoryAPIView,
   SearchWorkoutAPIView,
   SuggestedWorkoutAPIView,
   SuggestMealPlanAPIView
)

urlpatterns = [
    path("workouts/", WorkoutAPIView.as_view(), name="workouts"),
    path("suggested-workouts/", SuggestedWorkoutAPIView.as_view(), name="suggested-workouts"),
    path("meal-plan/", SuggestMealPlanAPIView.as_view(), name="meal-plan"),
    path("categories/", CategoryAPIView.as_view(), name="categories"),
    path("search-workout/", SearchWorkoutAPIView.as_view(), name="search-workout"),
    path("upload-body-image/", UploadBodyImageAPIView.as_view(), name="upload-body-image")
]
