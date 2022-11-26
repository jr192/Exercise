from django.test import TestCase

from api.models.barcode import Barcode
from api.models.order import Order
from api.services.barcode_service import BarcodeService
from api.tests.fixtures.factories.barcode_data import BarcodeDataFactory


class TestBarcodeService(TestCase):
    def setUp(self):
        self.barcode_data = BarcodeDataFactory()
        self.barcodes = []
        Order.objects.create(pk=1)

    def test_create_barcodes(self):
        BarcodeService().create_barcodes([self.barcode_data])

        barcode = Barcode.objects.filter(pk=self.barcode_data["barcode"])

        self.assertIsNotNone(barcode)

