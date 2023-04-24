from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(CarModel)
admin.site.register(Car)
admin.site.register(Order)
admin.site.register(Service)
admin.site.register(OrderRow)