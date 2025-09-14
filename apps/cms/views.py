import os
from rest_framework.views import APIView
from apps.utils.helpers import success, error
from apps.cms.models import Page
from .serializers import PageSerializer

class PageApiView(APIView):
    permission_classes = []

    def get(self, request):
        type = request.query_params.get("type", None)

        page = Page.objects.filter(type=type).first()

        serializer = PageSerializer(page)

        if page:
            return success(data=serializer.data, message="Page retrieved successfully")
        else:
            return success(data=[], message="Page not found", code=200)
