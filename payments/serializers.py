from rest_framework import serializers

from .models import Gateway


class GatewaySerializer(serializers.Serializer):
    class Meta:
        model = Gateway
        fields = '__all__'
