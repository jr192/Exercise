from django.test import TestCase

from api.models.customer import Customer
from api.models.order import Order
from api.services.order_service import OrderService
from api.tests.fixtures.factories.order_data import OrderDataFactory


class TestOrderService(TestCase):
    def setUp(self):
        self.order_data = OrderDataFactory()
        self.orders = []
        Customer.objects.create(pk=1)

    def test_create_barcodes(self):
        OrderService().create_orders([self.order_data])

        order = Order.objects.filter(pk=self.order_data["order_id"])

        self.assertIsNotNone(order)
