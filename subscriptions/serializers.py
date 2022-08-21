from rest_framework import serializers

from .models import Subscription, Package


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = '__all__'


class SubscriptionSerializer(serializers.ModelSerializer):
    package = PackageSerializer(many=False)

    class Meta:
        model = Subscription
        fields = ('package', 'expire_time', 'created_time')
