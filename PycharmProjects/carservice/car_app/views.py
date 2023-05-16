from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Car, OrderList, Order, Service, CarModel, OrderComment
from .forms import UserUpdateForm, ProfileUpdateForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import User
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages


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
        'orders': paged_orders,
    }
    return render(request, 'orders.html', context)


def order(request, order_list_id):
    order_list_orders = Order.objects.filter(order_list_id__exact=order_list_id)
    order_list = get_object_or_404(OrderList, pk=order_list_id)
    context = {
        'order_list_orders': order_list_orders,
        'order_list': order_list
    }

    if request.method == "POST":
        comment_request = request.POST['comment']
        comment = OrderComment(order_list_id=order_list_id, commenter=request.user, content=comment_request)
        comment.save()
        messages.info(request, f'Comment posted successfully')
        return redirect('order', order_list.order_list_id)
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


@login_required(login_url='login')
def client_orders(request):
    user = request.user
    try:
        user_orders = OrderList.objects.filter(client=request.user).order_by('due_back')
    except OrderList.DoesNotExist:
        user_orders = None
    context = {
        'user': user,
        'user_orders': user_orders,
    }
    return render(request, 'user_orders.html', context)


@csrf_protect
def register(request):
    if request.method == "POST":
        # taking all values from registration form
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # checking if passwords matches
        if password != password2:
            messages.error(request, 'Password does not match!')
            return redirect('register')

        # checking if username is not taken
        if User.objects.filter(username=username).exists():
            messages.error(request, f'Username {username} is taken! Choose another one')
            return redirect('register')

        # checking if email is not taken
        if User.objects.filter(email=email).exists():
            messages.error(request, f'User with {email} is already registered!')
            return redirect('register')

        # if everything is good, create new user.
        User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email,
                                 password=password)
        messages.info(request, f'User with username {username} registered!')
        return redirect('login')
    return render(request, 'registration/register.html')


@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Profile updated")
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'profile.html', context)
