import factory


class BarcodeDataFactory(factory.Factory):
    class Meta:
        model = dict

    order_id = 1
    barcode = 1110010
