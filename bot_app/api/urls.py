from django.urls import path
from bot_app.api.views import send_message_view


urlpatterns = [
    path('send-message/', send_message_view, name='send_message'),
]
