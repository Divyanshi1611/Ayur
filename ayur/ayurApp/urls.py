from django.urls import path
from .views import chat_view, gemini_chat_api, medicine_api

urlpatterns = [
    path('', chat_view, name='chat_view'),  # <-- change 'chat/' to ''
    path('api/gemini/', gemini_chat_api, name='gemini_chat_api'),
    path('api/medicine/', medicine_api, name='medicine_api'),
]