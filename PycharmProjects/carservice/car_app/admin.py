from django.contrib import admin
from .models import *


# Register your models here.


# class OrderRowAdmin(admin.ModelAdmin):
#     list_display = ('display_service', 'quantity', 'price')



admin.site.register(CarModel)
admin.site.register(Car)
admin.site.register(Order)
admin.site.register(Service)
admin.site.register(ServicePrice) #OrderRowAdmin
