from django.contrib import admin
from unfold.admin import ModelAdmin
from apps.ai_helper.models import SuggestedQuestion
from modeltranslation.admin import TranslationAdmin
from apps.ai_helper.models import ChatHistory
# Register your models here.
@admin.register(SuggestedQuestion)
class SuggestedQuestionAdmin(TranslationAdmin, ModelAdmin):
    list_display = ('id', 'question','question_en', 'question_de')
    list_display_links = ('id', 'question', 'question_en', 'question_de')
    search_fields = ('question',)
    ordering = ('id',)


@admin.register(ChatHistory)
class ChatHistoryAdmin(TranslationAdmin, ModelAdmin):
    list_display = ('id', 'user', 'question', 'answer', 'created_at')
    list_display_links = ('id', 'user', 'question', 'answer', 'created_at')
    search_fields = ('user__email', 'question', 'answer')
    ordering = ('-created_at',)