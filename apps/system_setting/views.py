from apps.system_setting.models import AboutSystem, Page
from rest_framework.views import APIView
from apps.system_setting.serializers import AboutSystemSerializer, PageSerializer
from apps.utils.helpers import success, error
# Create your views here.   

class AboutSystemAPIView(APIView):
    permission_classes = []
    def get(self, request):

        about_system = AboutSystem.objects.first()
   
        if about_system:
            serializer = AboutSystemSerializer(about_system)
            return success(serializer.data, "About system retrieved successfully.",200)
        return error(message="About system not found.", errors=None, status_code=404)


class PageAPIView(APIView):
    permission_classes = []
    def get(self, request):
        type = request.query_params.get("type", None)

        pages = Page.objects.filter(type=type) if type else Page.objects.all()

        serializer = PageSerializer(pages, many=True)
        return success(serializer.data, "Pages retrieved successfully.", 200)