from django.test import TestCase

from api.models.customer import Customer


class TestCustomerModel(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(pk=1)

    def test_orders_creation(self):

        self.assertEqual(1, self.customer.pk)
