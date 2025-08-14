from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Category, Workout
from django.utils.html import format_html

@admin.register(Category)
class CustomAdminClass(ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('name',)
    list_display_links = ('id', 'name',)



@admin.register(Workout)
class CustomWorkoutAdminClass(ModelAdmin):
    list_display = ('id', 'title', 'category', 'gender', 'play_video',)
    list_display_links = ('id', 'title', 'category', 'gender', 'play_video',)
    search_fields = ('title', 'category__name', 'gender',)
    list_filter = ('gender', 'category',)

    def play_video(self, obj):
        return format_html('<video width="150" height="80" controls><source src="{}" type="video/mp4">Your browser does not support the video tag.</video>', obj.video.url)