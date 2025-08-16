from django.urls import path

from django.conf.urls.static import static


from .views import (
   WorkoutAPIView
)

urlpatterns = [
    path("workouts/", WorkoutAPIView.as_view(), name="workouts"),
]
