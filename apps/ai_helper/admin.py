from django.contrib import admin
from unfold.admin import ModelAdmin
from apps.ai_helper.models import SuggestedQuestion
from apps.ai_helper.models import ChatHistory
# Register your models here.
@admin.register(SuggestedQuestion)
class SuggestedQuestionAdmin(ModelAdmin):
    list_display = ('id', 'question',)
    list_display_links = ('id', 'question',)
    search_fields = ('question',)
    ordering = ('id',)


@admin.register(ChatHistory)
class ChatHistoryAdmin(ModelAdmin):
    list_display = ('id', 'user', 'question', 'answer', 'created_at')
    list_display_links = ('id', 'user', 'question', 'answer', 'created_at')
    search_fields = ('user__email', 'question', 'answer')
    ordering = ('-created_at',)