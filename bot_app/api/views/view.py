from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from bot_app.api.serializers import MessageSerializer
from bot_app.logic.telegram_client import TelegramClient

@api_view(['POST'])
def send_message_view(request):
    serializer = MessageSerializer(data=request.data)

    if serializer.is_valid():
        chat_id = serializer.validated_data['chat_id']
        message = serializer.validated_data['message']

        telegram_client = TelegramClient()
        response = telegram_client.send_message(chat_id, message)

        if response['ok']:
            return Response({"message": "Message sent successfully"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Failed to send message"}, status=status.HTTP_400_BAD_REQUEST)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
