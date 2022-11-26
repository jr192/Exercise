import re

from django.db.models import Count
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from ..forms.files import UploadFileForm
from ..models.barcode import Barcode
from ..models.customer import Customer
from ..models.order import Order
from ..services.barcode_service import BarcodeService
from ..services.handle_file import HandleFile
from ..services.order_service import OrderService


@csrf_exempt
def order_view(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            order_data = HandleFile.handle_order_file(request.FILES["file"])
            OrderService().create_orders(order_data)
            return JsonResponse({"msg": "Import successfully."}, status=200)


@csrf_exempt
def barcode_view(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            barcode_data = HandleFile.handle_barcode_file(request.FILES["file"])
            BarcodeService.create_barcodes(barcode_data)
            return JsonResponse({"msg": "Import successfully."}, status=200)


def generate_file(request):
    if request.method == "GET":
        list_of_answers = []

        orders = list(Order.objects.all().values("pk"))

        top_five_customers = list(
            Customer.objects.annotate(order=Count("order_customer"))
            .order_by(("-order"))[:5]
            .values("id", "order")
        )

        unused_barcodes = Barcode.objects.filter(order=None).count()

        for order in orders:
            barcodes = list(
                Order.objects.annotate().values("barcode_order").filter(pk=order["pk"])
            )
            customer_id = list(
                Order.objects.annotate().filter(pk=order["pk"]).values("customer", "pk")
            )

            list_of_answers.append(str([*customer_id, *barcodes]))

        final_answer = [re.findall(r"\d+", answer) for answer in list_of_answers]

        print(
            "Top 5 customers that bought the most amount of tickets: ",
            top_five_customers,
        )
        print("Amount of unused barcodes: ", unused_barcodes)

        HandleFile().write_answer_to_file(final_answer)

        return JsonResponse(
            {"msg": "Please, check final answer at file file_with_answer.csv."},
            status=200,
        )
