from django.db import transaction

from api.models.barcode import Barcode
from api.models.customer import Customer
from api.models.order import Order
from rest_framework import serializers


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ["customer"]


class OrdersSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ["order_id"]


class BarcodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barcode
        fields = ["order"]


class Customer1Serializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    order = OrdersSerializer()
    barcode = BarcodeSerializer()

    class Meta:
        model = Customer
        fields = ["customer", "order", "barcode"]
