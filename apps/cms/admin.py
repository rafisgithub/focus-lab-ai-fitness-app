from django.contrib import admin
from django.db import models

# from apps.cms.forms import HowItWorkForm
from .models import (
    Brand,
    Feature,
    Footer,
    GlobalCta,
    Testimonial,
    Benefit,
    Faq,
    Page,
    HeroSection,
    HowItWorkFeature,
    HowItWork,
    InterviewCoachSection,
    UpcomingFeatureInterestedUser,
)
from import_export.admin import ImportExportModelAdmin
from unfold.contrib.import_export.forms import ExportForm

from unfold.admin import ModelAdmin
from django.utils.safestring import mark_safe
from django.utils.html import format_html
from .dropify import BrandForm, FeatureForm, TestimonialForm, BenefitForm, HowItWorkForm
from unfold.contrib.forms.widgets import WysiwygWidget


@admin.register(Brand)
class BrandAdmin(ModelAdmin):
    form = BrandForm

    list_display = ("serialNumber", "name_de", "name_en", "preview_logo")
    list_display_links = ("serialNumber", "name_de", "name_en", "preview_logo")
    search_fields = (
        "name_de",
        "name_en",
    )
    ordering = ("id",)

    fieldsets = ((None, {"fields": ("name", "logo")}),)

    def preview_logo(self, obj):
        if obj.logo:
            return format_html(
                '<img src="{}" style="max-height: 50px; max-width: 100px;" />',
                obj.logo.url,
            )
        return "No Logo"

    def serialNumber(self, obj):
        return obj.id

    serialNumber.short_description = "Serial Number"


@admin.register(Feature)
class FeatureAdmin(ModelAdmin):
    form = FeatureForm

    list_display = (
        "serialNumber",
        "title_de",
        "title_en",
        "short_description_de",
        "short_description_en",
        "preview_feature_logo",
    )
    list_display_links = (
        "serialNumber",
        "title_de",
        "title_en",
        "short_description_de",
        "short_description_en",
        "preview_feature_logo",
    )
    search_fields = (
        "title_de",
        "title_en",
        "short_description_de",
        "short_description_en",
    )
    ordering = ("id",)

    fieldsets = ((None, {"fields": ("title", "short_description", "logo")}),)

    def serialNumber(self, obj):
        return obj.id

    serialNumber.short_description = "Serial Number"

    def preview_feature_logo(self, obj):
        if obj.logo:
            return format_html(
                '<img src="{}" style="max-height: 50px; max-width: 100px;" />',
                obj.logo.url,
            )
        return "No Logo"


@admin.register(Testimonial)
class TestimonialAdmin(ModelAdmin):
    form = TestimonialForm

    list_display = (
        "serialNumber",
        "name_de",
        "name_en",
        "profession_de",
        "profession_en",
        "rating",
        "comment_de",
        "comment_en",
        "preview_user_image",
    )
    list_display_links = (
        "serialNumber",
        "name_de",
        "name_en",
        "profession_de",
        "profession_en",
        "rating",
        "preview_user_image",
    )
    search_fields = ("name_de", "name_en", "profession_de", "profession_en")
    ordering = ("id",)

    fieldsets = (
        (None, {"fields": ("name", "profession", "rating", "comment", "user_image")}),
    )

    def serialNumber(self, obj):
        return obj.id

    serialNumber.short_description = "Serial Number"

    def preview_user_image(self, obj):
        if obj.user_image:
            return format_html(
                '<img src="{}" style="max-height: 50px; max-width: 100px;" />',
                obj.user_image.url,
            )
        return "No Image"


@admin.register(Benefit)
class BenefitAdmin(ModelAdmin):
    form = BenefitForm

    list_display = (
        "serialNumber",
        "title_de",
        "title_en",
        "sub_title_de",
        "sub_title_en",
        "preview_benefit_logo",
    )
    list_display_links = (
        "serialNumber",
        "title_de",
        "title_en",
        "sub_title_de",
        "sub_title_en",
        "preview_benefit_logo",
    )
    search_fields = ("title_de", "title_en", "sub_title_de", "sub_title_en")
    ordering = ("id",)

    fieldsets = ((None, {"fields": ("title", "sub_title", "logo")}),)

    def serialNumber(self, obj):
        return obj.id

    serialNumber.short_description = "Serial Number"

    def preview_benefit_logo(self, obj):
        if obj.logo:
            return format_html(
                '<img src="{}" style="max-height: 50px; max-width: 100px;" />',
                obj.logo.url,
            )
        return "No Logo"


@admin.register(Faq)
class FaqAdmin(ModelAdmin):
    formfield_overrides = {
        models.TextField: {
            "widget": WysiwygWidget,
        }
    }
    list_display = (
        "serialNumber",
        "question_de",
        "question_en",
        "answer_de",
        "answer_en",
        "is_active",
    )
    list_display_links = (
        "serialNumber",
        "question_de",
        "question_en",
        "answer_de",
        "answer_en",
        "is_active",
    )
    search_fields = ("question_de", "question_en")
    ordering = ("id",)

    fieldsets = ((None, {"fields": ("question", "answer", "is_active")}),)

    def serialNumber(self, obj):
        return obj.id

    serialNumber.short_description = "Serial Number"


@admin.register(Page)
class PageAdmin(ModelAdmin):
    formfield_overrides = {
        models.TextField: {
            "widget": WysiwygWidget,
        }
    }

    list_display = ("serialNumber", "type", "title_de", "title_en", "is_active")
    list_display_links = ("serialNumber", "type", "title_de", "title_en", "is_active")
    search_fields = ("title_de", "title_en", "type")
    ordering = ("id",)

    fieldsets = ((None, {"fields": ("type", "title", "content", "is_active")}),)

    def serialNumber(self, obj):
        return obj.id

    serialNumber.short_description = "Serial Number"


@admin.register(HeroSection)
class HeroSectionAdmin(ModelAdmin):
    list_display = ("serialNumber", "title", "sub_title", "preview_banner")
    list_display_links = ("serialNumber", "title", "sub_title", "preview_banner")
    search_fields = ("title", "sub_title")
    ordering = ("id",)

    fieldsets = ((None, {"fields": ("title", "sub_title", "banner")}),)

    def has_add_permission(self, request):
        return False

    def serialNumber(self, obj):
        return obj.id

    serialNumber.short_description = "Serial Number"

    def preview_banner(self, obj):
        if obj.banner:
            return format_html(
                '<img src="{}" style="max-height: 50px; max-width: 100px;" />',
                obj.banner.url,
            )
        return "No Banner"


@admin.register(HowItWorkFeature)
class FeatureAdmin(ModelAdmin):
    list_display = ("serialNumber", "name_en", "name_de")
    list_display_links = ("serialNumber", "name_en", "name_de")
    search_fields = ("name_en", "name_de")
    ordering = ("id",)

    fieldsets = ((None, {"fields": ("name",)}),)

    def serialNumber(self, obj):
        return obj.id

    serialNumber.short_description = "Serial Number"


@admin.register(HowItWork)
class HowItWorkAdmin(ModelAdmin):
    model = HowItWork
    form = HowItWorkForm
    list_display = (
        "serialNumber",
        "title",
        "sub_title",
        "short_description",
        "preview_side_image",
    )
    list_display_links = (
        "serialNumber",
        "title",
        "sub_title",
        "short_description",
        "preview_side_image",
    )
    search_fields = ("title", "sub_title", "short_description")
    ordering = ("id",)

    fieldsets = ((None, {"fields": ("title", "sub_title", "side_image", "features")}),)

    def serialNumber(self, obj):
        return obj.id

    serialNumber.short_description = "Serial Number"

    def preview_side_image(self, obj):
        if obj.side_image:
            return format_html(
                '<img src="{}" style="max-height: 50px; max-width: 100px;" />',
                obj.side_image.url,
            )
        return "No Side Image"


@admin.register(InterviewCoachSection)
class InterviewCoachSectionAdmin(ModelAdmin):
    list_display = ("serialNumber", "title_en", "short_description")
    list_display_links = ("serialNumber", "title_en", "short_description")
    search_fields = ("title_en",)
    ordering = ("id",)

    fieldsets = ((None, {"fields": ("title", "short_description")}),)

    def serialNumber(self, obj):
        return obj.id

    serialNumber.short_description = "Serial Number"

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Footer)
class FooterAdmin(ModelAdmin):
    list_display = (
        "serialNumber",
        "content_en",
        "content_de",
        "copyright_text_en",
        "copyright_text_de",
    )
    list_display_links = (
        "serialNumber",
        "content_en",
        "content_de",
        "copyright_text_en",
        "copyright_text_de",
    )
    search_fields = (
        "content_en",
        "content_de",
        "copyright_text_en",
        "copyright_text_de",
    )
    ordering = ("id",)

    fieldsets = ((None, {"fields": ("content", "copyright_text")}),)

    def serialNumber(self, obj):
        return obj.id

    serialNumber.short_description = "Serial Number"

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(UpcomingFeatureInterestedUser)
class UpcomingFeatureInterestedUserAdmin(ModelAdmin, ImportExportModelAdmin):
    export_form_class = ExportForm
    list_display = ("serialNumber", "email")
    list_display_links = ("serialNumber", "email")
    search_fields = ("email",)
    ordering = ("id",)

    def serialNumber(self, obj):
        return obj.id

    serialNumber.short_description = "Serial Number"

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_import_permission(self, request):
        return False
    
@admin.register(GlobalCta)
class GlobalCtaAdmin(ModelAdmin):
    list_display = ("serialNumber", "title_en", "title_de", "description_en", "button_text_en", "button_text_de")
    list_display_links =("serialNumber", "title_en", "title_de", "description_en", "button_text_en", "button_text_de")
    search_fields =("serialNumber", "title_en", "title_de", "description_en", "button_text_en", "button_text_de")
    ordering = ("id",)

    fieldsets = ((None, {"fields": ("title", "description", "button_text")}),)

    def serialNumber(self, obj):
        return obj.id

    serialNumber.short_description = "Serial Number"
