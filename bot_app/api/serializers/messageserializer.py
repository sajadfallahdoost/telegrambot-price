from rest_framework import serializers


class MessageSerializer(serializers.Serializer):
    chat_id = serializers.CharField(max_length=100)
    message = serializers.CharField(max_length=500)

    def validate(self, data):
        if len(data['message']) > 500:
            raise serializers.ValidationError("Message is too long")
        return data
