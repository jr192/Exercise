from django.contrib import admin

from api.models.customer import Customer
from api.models.order import Order
from api.models.barcode import Barcode

admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Barcode)
