from django.db import models

from api.models.customer import Customer


class Order(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, null=True, related_name="order_customer"
    )
