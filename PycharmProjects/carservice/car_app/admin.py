from django.contrib import admin
from .models import *


# Register your models here.


class OrderInline(admin.TabularInline):
    model = Order
    # Turn off extra empty lines for input
    extra = 0


class OrderListAdmin(admin.ModelAdmin):
    list_display = ('car', 'order_date')
    inlines = [OrderInline]


class CarAdmin(admin.ModelAdmin):
    list_display = ('client', 'licence_plate', 'car_model', 'vin_code')
    list_filter = ('client', 'car_model')
    search_fields = ('licence_plate', 'vin_code', 'client')


class ServicePriceAdmin(admin.ModelAdmin):
    list_display = ('service', 'price')


admin.site.register(CarModel)
admin.site.register(Car, CarAdmin)
admin.site.register(Service)
admin.site.register(ServicePrice, ServicePriceAdmin)
admin.site.register(OrderList, OrderListAdmin)
admin.site.register(Order)
