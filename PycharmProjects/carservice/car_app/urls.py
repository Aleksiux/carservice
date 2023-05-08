from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cars', views.cars, name='cars'),
    path('car/<int:car_id>', views.car, name='car'),
    path('orders/', views.orders, name='orders'),
    path('order/<int:order_list_id>', views.order, name='order'),
    path('search/', views.search, name='search'),
    path('account/', include('django.contrib.auth.urls')),
]
