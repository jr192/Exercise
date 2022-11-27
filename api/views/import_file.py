from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from ..forms.files import UploadFileForm
from ..services.answers_service import AnswersClass
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

        AnswersClass().bonus_points_answer()

        final_answer = AnswersClass().creating_data_for_file(list_of_answers)

        HandleFile().write_answer_to_file(final_answer)

        return JsonResponse(
            {"msg": "Please, check final answer at file file_with_answer.csv."},
            status=200,
        )
