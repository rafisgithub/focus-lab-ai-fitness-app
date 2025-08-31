
from rest_framework import fields, serializers
from apps.cms.models import Page

class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ['title', 'content', 'type']
