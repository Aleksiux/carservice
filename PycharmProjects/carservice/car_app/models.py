from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone


# Create your models here.


class CarModel(models.Model):
    car_model_id = models.AutoField(primary_key=True)
    brand = models.CharField('Car brand', max_length=50)
    car_model = models.CharField('Car model', max_length=50)
    year = models.DateField('Car year')
    engine = models.CharField('Car engine', max_length=20)

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

    def __str__(self):
        return f"{self.licence_plate} {self.car_model} {self.vin_code} {self.client}"

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


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    date = models.DateTimeField('Date', default=timezone.now)
    car = models.ForeignKey(Car, null=True, on_delete=models.SET_NULL)
    service = models.ForeignKey(Service, null=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField('Quantity')
    total_price = models.IntegerField('Total Amount')

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        ordering = ['date']

    def __str__(self):
        return f"{self.date} {self.total_price}"

# class OrderInstance(models.Model):
#     order_instance_id = models.AutoField(primary_key=True)
#     order = models.ForeignKey(Order, null=True, on_delete=models.SET_NULL)
#     service = models.ForeignKey(Service, null=True, on_delete=models.SET_NULL)
#     quantity = models.IntegerField('Quantity')
#     price = models.FloatField('Price')
