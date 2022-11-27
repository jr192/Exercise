import re
from django.db.models import Count

from api.models.barcode import Barcode
from api.models.customer import Customer
from api.models.order import Order


class AnswersClass:
    @classmethod
    def bonus_points_answer(cls):
        top_five_customers = list(
            Customer.objects.annotate(order=Count("order_customer"))
            .order_by(("-order"))[:5]
            .values("id", "order")
        )

        unused_barcodes = Barcode.objects.filter(order=None).count()

        print(
            "Top 5 customers that bought the most amount of tickets by customer_id and number of tickets:"
        )
        for customer in top_five_customers:
            print(f'{customer["id"]}, {customer["order"]}')

        print("Amount of unused barcodes: ", unused_barcodes)

    @classmethod
    def creating_data_for_file(cls, list_of_answers):
        orders = list(Order.objects.all().values("pk"))

        for order in orders:
            barcodes = list(
                Order.objects.annotate().values("barcode_order").filter(pk=order["pk"])
            )
            customer_id = list(
                Order.objects.annotate().filter(pk=order["pk"]).values("customer", "pk")
            )

            list_of_answers.append(str([*customer_id, *barcodes]))

        final_answer = [re.findall(r"\d+", answer) for answer in list_of_answers]

        return final_answer
