from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import User, UserProfile
from django.utils.html import format_html
@admin.register(User)
class CustomAdminClass(ModelAdmin):
    list_display = ('id', 'email', 'full_name', 'preview_user_image', 'gender')
    list_display_links = ('id', 'email', 'full_name', 'preview_user_image', 'gender')
    search_fields = ('email', 'full_name')
    list_filter = ('gender',)
    def full_name(self, obj):
        return obj.profile.full_name if hasattr(obj, 'profile') else ''

    def last_name(self, obj):
        return obj.profile.last_name if hasattr(obj, 'profile') else ''


    def preview_user_image(self, obj):
        if obj.profile.avatar:
            return format_html('<img src="{}" style="max-height: 50px; max-width: 50px;" />', obj.profile.avatar.url)
        return "No Image"

@admin.register(UserProfile)
class ProfileAdmin(ModelAdmin):
    pass