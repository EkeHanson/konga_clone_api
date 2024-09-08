from rest_framework import serializers
from .models import Withdraw
from django.utils import timezone
from datetime import timedelta
from django.db.models import Sum

class WithdrawSerializer(serializers.ModelSerializer):
    class Meta:
        model = Withdraw
        fields = '__all__'

