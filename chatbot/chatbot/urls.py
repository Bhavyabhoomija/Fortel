from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect  #  Add this import

def home_redirect(request):
    return redirect('/chat/')  # Redirect root URL to /chat/

urlpatterns = [
    path('', home_redirect),  #  Redirect root to chat
    path('admin/', admin.site.urls),
    path('chat/', include('chatbot1.urls')),
]
