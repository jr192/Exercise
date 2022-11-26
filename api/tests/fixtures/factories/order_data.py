import factory


class OrderDataFactory(factory.Factory):
    class Meta:
        model = dict

    customer = 1
    order_id = 1
