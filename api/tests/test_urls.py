from django.test import SimpleTestCase, RequestFactory
from django.urls import reverse, resolve

from Tiqets.settings import API_ORDER_URL, API_BARCODE_URL


class TestUrlsView(SimpleTestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_order_url(self):
        url = reverse("order_view")
        self.assertEqual(url, API_ORDER_URL)

    def test_barcode_url(self):
        url = reverse("barcode_view")
        self.assertEqual(url, API_BARCODE_URL)

    def test_connection_to_order_view(self):
        resolver = resolve(API_ORDER_URL)
        self.assertEqual(resolver.view_name, "order_view")

    def test_connection_to_barcode_view(self):
        resolver = resolve(API_BARCODE_URL)
        self.assertEqual(resolver.view_name, "barcode_view")
