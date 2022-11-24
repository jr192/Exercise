from django.urls import path
from rest_framework import routers

from api.views.import_file import barcode_view, order_view, generate_file

router = routers.DefaultRouter()


urlpatterns = [
    path("order/", order_view, name="order_view"),
    path("barcode/", barcode_view, name="barcode_view"),
    path("file/", generate_file, name="generate_file"),
]
