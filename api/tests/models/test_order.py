from django.test import TestCase

from api.models.customer import Customer
from api.models.order import Order


class TestOrderModel(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(pk=1)
        Order.objects.create(pk=1, customer=self.customer)

    def test_orders_creation(self):
        order_created = Order.objects.get(pk=1)

        self.assertEqual(1, order_created.customer_id)
