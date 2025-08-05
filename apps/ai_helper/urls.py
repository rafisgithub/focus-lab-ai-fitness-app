"""Module providing URL patterns for the AI helper app."""

from django.urls import path
from .views import SuggestedQuestionAPIView, ChatHistoryAPIView, ChatsAPIView, CreateResumeAPIView,ResumeHistoryAPIView, CreateCoverLetterAPIView, CoverLetterHistoryAPIView


urlpatterns = [
    path("suggested-questions/", SuggestedQuestionAPIView.as_view(), name="suggested_questions"),
    path("chat-histories/", ChatHistoryAPIView.as_view(), name="chat_histories"),
    path("chats/", ChatsAPIView.as_view(), name="chats"),
    path("create-resume/", CreateResumeAPIView.as_view(), name="create_resume"),
    path("resume-histories/", ResumeHistoryAPIView.as_view(), name="resume_histories"),
    path("create-cover-letter/", CreateCoverLetterAPIView.as_view(), name="create_cover_letter"),
    path("cover-letter-histories/", CoverLetterHistoryAPIView.as_view(), name="cover_letter_histories"),
]
