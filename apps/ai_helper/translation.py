from modeltranslation.translator import register, TranslationOptions
from .models import  SuggestedQuestion, ChatHistory

@register(SuggestedQuestion)
class SuggestedQuestionTranslationOptions(TranslationOptions):
    fields = ('question',)

@register(ChatHistory)
class ChatHistoryTranslationOptions(TranslationOptions):
    fields = ('question', 'answer')