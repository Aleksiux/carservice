from django.contrib import admin
from .models import *


# Register your models here.


class CarAdmin(admin.ModelAdmin):
    list_display = ('client', 'licence_plate', 'car_model', 'vin_code')
    list_filter = ('client', 'car_model')
    search_fields = ('licence_plate', 'vin_code', 'client')


admin.site.register(CarModel)
admin.site.register(Car, CarAdmin)
admin.site.register(Order)
admin.site.register(Service)
admin.site.register(ServicePrice)  # OrderRowAdmin
