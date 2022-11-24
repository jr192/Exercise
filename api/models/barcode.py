from django.db import models

from api.models.order import Order


class Barcode(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.DO_NOTHING, null=True, related_name="barcode_order"
    )
