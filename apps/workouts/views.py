from apps.workouts.models import Workout
from rest_framework.views import APIView
from apps.workouts.serializers import WorkoutSerializer
from apps.utils.helpers import success, error
from rest_framework.permissions import IsAuthenticated


class WorkoutAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        gender = user.gender

        category_id = request.query_params.get("category_id", None)
        print(category_id)

        workouts = Workout.objects.filter(category=category_id, gender=gender) if category_id else Workout.objects.all()

        serializer = WorkoutSerializer(workouts, many=True)
        print(serializer.data)
        return success(serializer.data, "Workouts retrieved successfully.", 200)