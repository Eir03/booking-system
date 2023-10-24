from django.db import models
from djmoney.models.fields import MoneyField

class Service(models.Model):
    name = models.CharField('Наименование услуги', blank=True, max_length=100)
    price = MoneyField('Стоимость', max_digits=10, decimal_places=2, default_currency='RUB')

class RoomType(models.Model):
    name = models.CharField('Наименование', max_length=100)
    image = models.ImageField('Изображение', blank=True, null=True)

class Room(models.Model):
    number = models.CharField('Номер', max_length=5)
    type = models.ForeignKey('RoomType', verbose_name='Тип номера', on_delete=models.CASCADE)
    max_occupancy = models.PositiveSmallIntegerField('Количество мест')
    price = MoneyField('Стоимость', max_digits=10, decimal_places=2, default_currency='RUB')

class Reservation(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    occupancy = models.PositiveSmallIntegerField()
    total_price = MoneyField('Стоимость', max_digits=10, decimal_places=2, default_currency='RUB')
    services = models.ManyToManyField(Service)