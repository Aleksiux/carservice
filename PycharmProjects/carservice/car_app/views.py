from django.shortcuts import render, get_object_or_404
from .models import Car, OrderList, Order, Service, CarModel


# Create your views here.
def index(request):
    cars = CarModel.objects.all().values('brand')
    orders_count = OrderList.objects.all().count()
    cars_count = Car.objects.all().count()
    services = Service.objects.all()
    services_count = Service.objects.all().count()
    context = {
        'cars':cars,
        'orders_count': orders_count,
        'car_count': cars_count,
        'services': services,
        'services_count': services_count
    }
    return render(request, 'index.html', context)


def cars(request):
    cars = Car.objects.all()
    context = {
        'cars': cars,
    }
    return render(request, 'car_models.html', context)


def car(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    context = {
        'car': car
    }
    return render(request, 'car.html', context)


def orders(request):
    orders = OrderList.objects.all()
    context = {
        'orders': orders
    }
    return render(request, 'orders.html', context)


def order(request, order_list_id):
    order_list = Order.objects.filter(order_list_id__exact=order_list_id)
    context = {
        'order_list': order_list
    }
    return render(request, 'order.html', context)
