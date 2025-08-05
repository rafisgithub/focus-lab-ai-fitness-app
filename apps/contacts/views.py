from rest_framework.views import APIView
from rest_framework.response import Response

from django.utils import translation
from .serializers import ContactUsSerializer
from .models import Contact
from apps.utils.helpers import success, error
# Create your views here.

class ContactUsAPIView(APIView):    

    def post(self, request):
        try:
            serializer = ContactUsSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return success(data=serializer.data, message="Contact form submitted successfully")
            else:
                return error(message="Invalid data", errors=serializer.errors)
        except Exception as e:
            return error(message="Failed to submit contact form", errors=str(e))