from django.contrib import admin
from unfold.admin import ModelAdmin

from apps.contacts.models import Contact
from import_export.admin import ImportExportModelAdmin
from unfold.contrib.import_export.forms import ExportForm
from django.utils.html import format_html
@admin.register(Contact)
class ContactAdmin(ModelAdmin, ImportExportModelAdmin):
    export_form_class = ExportForm
    list_display = ('id', 'first_name', 'last_name', 'email', 'phone_number', 'message', 'agree_terms','read_status_badge')
    list_display_links = ('id', 'first_name', 'last_name', 'email', 'phone_number', 'message', 'agree_terms')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('created_at','is_read',)

    def has_add_permission(self, request):
        return False
    
    def has_change_permission(self, request, obj = None):
        return False
    
    def has_delete_permission(self, request, obj = None):
        return False
    
    def has_import_permission(self, request):
        return False 
    
    def read_status_badge(self, obj):
        if obj.is_read:
            return format_html('<span style="color:white; background-color:green; padding:2px 6px; border-radius:4px;">Read</span>')
        return format_html('<span style="color:white; background-color:red; padding:2px 6px; border-radius:4px;">Unread</span>')

    read_status_badge.short_description = 'Status'

    def change_view(self, request, object_id, form_url='', extra_context=None):
        obj = self.get_object(request, object_id)
        if obj and not obj.is_read:
            obj.is_read = True
            obj.save()
        return super().change_view(request, object_id, form_url, extra_context)