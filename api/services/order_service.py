from api.models.customer import Customer
from api.models.order import Order


class OrderService:
    @classmethod
    def create_orders(cls, order_data):
        customers = []
        orders = []

        for customer in order_data:
            customers.append(Customer(pk=customer["customer"]))

        Customer.objects.bulk_create(customers, ignore_conflicts=True)

        for order in order_data:
            customer = Customer(pk=order["customer"])
            orders.append(Order(pk=order["order_id"], customer=customer))

        Order.objects.bulk_create(orders)
