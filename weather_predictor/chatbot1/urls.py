from django.urls import path
from .views import chat

urlpatterns = [
    path('', chat, name='chat'),  # Now accessible at `/api/chat/`
]
