from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import User
from django.utils.html import format_html

@admin.register(User)
class CustomAdminClass(ModelAdmin):

    list_display = ('id', 'email', 'first_name', 'last_name', 'preview_user_image', 'is_staff', 'is_active')
    list_display_links = ('id', 'email', 'first_name', 'last_name', 'preview_user_image', 'is_staff', 'is_active')
    search_fields = ('email', 'first_name', 'last_name')

    def first_name(self, obj):
        return obj.profile.first_name if hasattr(obj, 'profile') else ''

    def last_name(self, obj):
        return obj.profile.last_name if hasattr(obj, 'profile') else ''


    def preview_user_image(self, obj):
        if obj.profile.profile_image:
            return format_html('<img src="{}" style="max-height: 50px; max-width: 100px;" />', obj.profile.profile_image.url)
        return "No Image"