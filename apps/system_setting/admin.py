from django.contrib import admin
from django.utils.html import format_html
from unfold.admin import ModelAdmin
from .models import AboutSystem, DynamicPages, SMTPSetting, SocialMedia
@admin.register(AboutSystem)

class AboutSystemAdmin(ModelAdmin):
    list_display = ("id", "name", "title", "email", "copyright", "preview_logo", "preview_favicon", "description",)
    search_fields = ("id", "name", "title", "email", "copyright", "preview_logo", "preview_favicon", "description",)
    list_display_links = ("id", "name", "title", "email", "copyright", "preview_logo", "preview_favicon", "description",)

    def has_add_permission(self, request):
        return False

    def preview_logo(self, obj):
        if obj.logo:
            return format_html(f'<img src="{obj.logo.url}" width="50" height="50" />')
        return "No Logo"

    def preview_favicon(self, obj):
        if obj.favicon:
            return format_html(f'<img src="{obj.favicon.url}" width="50" height="50" />')
        return "No Favicon"

@admin.register(DynamicPages)
class DynamicPagesAdmin(ModelAdmin):
    list_display = ("id", "title", "status",)
    search_fields = ("id", "title", "content",)
    list_display_links = ("id", "title", "status",)

@admin.register(SMTPSetting)
class SMTPSettingAdmin(ModelAdmin):
  

    list_display = ("id", "host", "port", "username", "encryption", "sender_name", "sender_email", "is_active",)
    search_fields = ("id", "host", "username", "sender_name", "sender_email",)
    list_display_links = ("id", "host", "username", "sender_name", "sender_email",)

    def has_add_permission(self, request):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(SocialMedia)
class SocialMediaAdmin(ModelAdmin):
    list_display = ("id", "name", "url", "preview_icon",)
    search_fields = ("id", "name", "url", "preview_icon",)
    list_display_links = ("id", "name", "url","preview_icon",)


    def preview_icon(self, obj):
        if obj.icon:
            return format_html(f'<img src="{obj.icon.url}" width="50" height="50" />')
        return "No Icon"