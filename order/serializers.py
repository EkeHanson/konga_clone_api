from rest_framework import serializers
from .models import OrderGrabbing


class OrderGrabbingSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderGrabbing
        fields = '__all__'

