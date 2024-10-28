import uuid
from django.db import models
from django.contrib.auth.models import User

class RestaurantOrder(models.Model):
    order_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)  # UUID for unique order ID
    sr_no = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=255, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    instruction = models.TextField(blank=True)
    date = models.DateField(null=True, blank=True)

    @property
    def total_price(self):
        return self.price * self.quantity if self.price and self.quantity else 0

    def __str__(self):
        return f"Order {self.order_id} - {self.item_name}"
