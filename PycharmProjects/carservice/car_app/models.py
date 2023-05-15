from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from django_resized import ResizedImageField
from PIL import *
from django.contrib.auth.models import User
from datetime import date
from tinymce.models import HTMLField


# Create your models here.


class CarModel(models.Model):
    car_model_id = models.AutoField(primary_key=True)
    brand = models.CharField('Car brand', max_length=50)
    car_model = models.CharField('Car model', max_length=50)
    year = models.DateField('Car year')
    engine = models.CharField('Car engine', max_length=20)
    car_photo = ResizedImageField('Car photo', size=[375, 500], upload_to='car_photo', null=True)

    class Meta:
        verbose_name = 'Car model'
        verbose_name_plural = 'Car models'
        ordering = ['brand']

    def __str__(self):
        return f"{self.brand} {self.car_model} {self.year} {self.engine}"


class Car(models.Model):
    car_id = models.AutoField(primary_key=True)
    licence_plate = models.CharField('Licence plate', max_length=50)
    car_model = models.ForeignKey(CarModel, null=True, on_delete=models.SET_NULL)
    vin_code = models.CharField('VIN code', max_length=17)
    client = models.CharField('Client', max_length=100, help_text='Enter client:')
    description = HTMLField('Description', help_text='Enter author description:', null=True)

    def __str__(self):
        return f"{self.licence_plate} {self.car_model} {self.client}"

    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'


class Service(models.Model):
    """Service table"""
    service_id = models.AutoField(primary_key=True)
    name = models.CharField('Service name', max_length=100, help_text='Enter service name:')
    price = models.IntegerField('Service price ', help_text='Enter service price:')

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
        ordering = ['name']

    def __str__(self):
        return f"{self.name}"


class ServicePrice(models.Model):
    service_price_id = models.AutoField(primary_key=True)
    service = models.ForeignKey(Service, null=True, on_delete=models.SET_NULL)
    cars = models.ManyToManyField(CarModel)
    price = models.IntegerField('Price')

    class Meta:
        verbose_name = 'Service price'
        verbose_name_plural = 'Service prices'
        ordering = ['service_price_id']

    def __str__(self):
        return f"{self.service} {self.price}"


class OrderList(models.Model):
    """Order list which is connected to an order. Representing the visit to the car service
    and the total order placed """
    order_list_id = models.AutoField(primary_key=True)
    order_date = models.DateField('Order date', null=True, blank=True)
    car = models.ForeignKey(Car, null=True, on_delete=models.SET_NULL)
    # total_price = models.FloatField('Total Amount')
    due_back = models.DateField('Return date', null=True, blank=True)
    client = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def total_order_list_price(self):
        total_sum = 0
        orders = self.orders.filter(order_list_id__exact=self.order_list_id)
        for order in orders:
            total_sum += order.total_price
        return total_sum

    ORDER_STATUS = (
        ('n', 'Not started'),
        ('i', 'In progress'),
        ('d', 'Done'),
    )
    order_status = models.CharField(max_length=1, default='n', blank=True, choices=ORDER_STATUS,
                                    help_text='Order status')

    @property
    def is_overdue(self):
        if date.today() > self.order_date:
            return True
        return False

    class Meta:
        verbose_name = 'Order List'
        verbose_name_plural = 'Order Lists'

    def __str__(self):
        return f"{self.car} - {self.order_date}"


class Order(models.Model):
    """Order which is connected to an order list. Representing one service/thing bought."""
    order_id = models.AutoField(primary_key=True)
    order_list_id = models.ForeignKey(OrderList, on_delete=models.SET_NULL, null=True, related_name='orders')
    service = models.ForeignKey(Service, null=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField('Quantity')
    price = models.FloatField('Price')

    @property
    def total_price(self):
        return self.price * self.quantity

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f"{self.quantity} - {self.price}"


class OrderComment(models.Model):
    order_comment_id = models.AutoField(primary_key=True)
    order_list = models.ForeignKey(OrderList, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='order_list')
    commenter = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    content = models.TextField('Content', max_length=2000)

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = 'Comment'
        ordering = ['-date_created']
