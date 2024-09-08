from rest_framework import viewsets, permissions
from .models import BankDetail
from .serializers import BankDetailSerializer

class BankDetailViewSet(viewsets.ModelViewSet):
    queryset = BankDetail.objects.all()
    serializer_class = BankDetailSerializer
    permission_classes = [permissions.AllowAny]  # Allows access to anyone

