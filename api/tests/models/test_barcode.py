from django.test import TestCase

from api.models.barcode import Barcode
from api.models.customer import Customer
from api.models.order import Order


class TestBarcodeModel(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(pk=1)
        self.order = Order.objects.create(pk=1, customer=self.customer)
        Barcode.objects.create(pk=1, order=self.order)

    def test_orders_creation(self):
        barcode_created = Barcode.objects.get(pk=1)

        self.assertEqual(1, self.order.customer_id)
        self.assertEqual(1, self.order.pk)
        self.assertEqual(1, barcode_created.pk)
