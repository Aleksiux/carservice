from django.contrib import admin
from .models import Order, Profile, OrderComment, OrderList, CarModel, Car, Service, ServicePrice


# Register your models here.


class OrderInline(admin.TabularInline):
    model = Order
    # Turn off extra empty lines for input
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = ('total_price',)

    def total_price(self, obj):
        return obj.total_price


class OrderListAdmin(admin.ModelAdmin):
    list_display = ('car', 'order_date', 'total_orderlist_price', 'client', 'due_back')
    inlines = [OrderInline]

    def total_orderlist_price(self, obj):
        return obj.total_order_list_price


class CarAdmin(admin.ModelAdmin):
    list_display = ('client', 'licence_plate', 'car_model', 'vin_code')
    list_filter = ('client', 'car_model')
    search_fields = ('licence_plate', 'vin_code', 'client')


class ServicePriceAdmin(admin.ModelAdmin):
    list_display = ('service', 'price')


class OrderListCommentAdmin(admin.ModelAdmin):
    list_display = ('order_list', 'date_created', 'commenter', 'content')

admin.site.register(Profile)
admin.site.register(OrderComment, OrderListCommentAdmin)
admin.site.register(CarModel)
admin.site.register(Car, CarAdmin)
admin.site.register(Service)
admin.site.register(ServicePrice, ServicePriceAdmin)
admin.site.register(OrderList, OrderListAdmin)
admin.site.register(Order, OrderAdmin)
