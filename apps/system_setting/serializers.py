from rest_framework import serializers
from .models import AboutSystem, Page

class AboutSystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutSystem
        fields = "__all__"


class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = "__all__"