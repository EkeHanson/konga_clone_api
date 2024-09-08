from django.db import models

# Create your models here.
from django.db import models
from django.core.exceptions import ValidationError

class BankDetail(models.Model):
    bank_name = models.CharField(max_length=100, default="Access Diamond Bank PLC")
    account_number = models.CharField(max_length=20, default= "0063193061")
    recipient_name = models.CharField(max_length=100, default= "Abraham Ekene-onwon Hanson")


    def __str__(self):
        return f"{self.recipient_name} - {self.bank_name}"

    def save(self, *args, **kwargs):
        # Check if any instance of BankDetail already exists
        if BankDetail.objects.exists() and not self.pk:
            raise ValidationError("Only one BankDetail instance is allowed.")
        return super(BankDetail, self).save(*args, **kwargs)

