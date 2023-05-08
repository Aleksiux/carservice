from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Car, OrderList, Order, Service, CarModel
from django.db.models import Q


# Create your views here.
def index(request):
    cars = CarModel.objects.all().values('brand')
    orders_count = OrderList.objects.all().count()
    cars_count = Car.objects.all().count()
    services = Service.objects.all()
    services_count = Service.objects.all().count()
    number_of_visits = request.session.get('number_of_visits', 1)
    request.session['number_of_visits'] = number_of_visits + 1
    context = {
        'cars': cars,
        'orders_count': orders_count,
        'car_count': cars_count,
        'services': services,
        'services_count': services_count,
        'number_of_visits': number_of_visits
    }
    return render(request, 'index.html', context)


def cars(request):
    paginator = Paginator(Car.objects.all(), 2)
    page_number = request.GET.get('page')
    paged_cars = paginator.get_page(page_number)
    context = {
        'cars': paged_cars,
    }
    return render(request, 'car_models.html', context)


def car(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    context = {
        'car': car
    }
    return render(request, 'car.html', context)


def orders(request):
    paginator = Paginator(OrderList.objects.all(), 2)
    page_number = request.GET.get('page')
    paged_orders = paginator.get_page(page_number)
    context = {
        'orders': paged_orders
    }
    return render(request, 'orders.html', context)


def order(request, order_list_id):
    order_list_orders = Order.objects.filter(order_list_id__exact=order_list_id)
    order_list = get_object_or_404(OrderList, pk=order_list_id)
    print(order_list)
    context = {
        'order_list_orders':order_list_orders,
        'order_list': order_list
    }
    return render(request, 'order.html', context)


def search(request):
    """
    Simple search. query takes information from search form,
    search_results filters by input text, car client, car model, license plate and VIN.
    Icontains from contains different that icontains is not key sensitive.
    """
    query = request.GET.get('query')

    search_results = Car.objects.filter(
        Q(client__icontains=query) | Q(car_model__car_model__icontains=query) | Q(licence_plate__icontains=query) | Q(
            vin_code__icontains=query))
    print(search_results)
    return render(request, 'search.html', {'cars': search_results, 'query': query})
