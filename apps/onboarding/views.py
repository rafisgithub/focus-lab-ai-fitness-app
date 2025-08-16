from rest_framework.views import APIView
from apps.utils.helpers import success, error



class OnboardingView(APIView):
    
    permission_classes = []

    def post(self, request, *args, **kwargs):
        data = request.data

        return success(data=data,message="Onboarding successful")