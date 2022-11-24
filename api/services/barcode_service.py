from api.models.barcode import Barcode
from api.models.order import Order


class BarcodeService:
    @classmethod
    def create_barcodes(cls, barcode_data):
        barcodes = []

        for barcode in barcode_data:
            order = Order(pk=barcode["order_id"])
            barcodes.append(Barcode(pk=barcode["barcode"], order=order))

        Barcode.objects.bulk_create(barcodes, ignore_conflicts=False)
