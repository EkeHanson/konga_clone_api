from django.db import models
from account.models import CustomUser


class OrderGrabbing(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    commission = models.DecimalField(max_digits=10, decimal_places=2)
    grabbed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.phone} grabbed Order {self.order.id}"

    def save(self, *args, **kwargs):
   
        self.user.grabbed_orders_count += 1
        self.user.save()

        super().save(*args, **kwargs)


