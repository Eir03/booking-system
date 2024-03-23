from django.db import models
from djmoney.models.fields import MoneyField
from .admin import register_model
@register_model
class Service(models.Model):
    name = models.CharField('Наименование услуги', blank=True, max_length=100)
    price = MoneyField('Стоимость', max_digits=10, decimal_places=2, default_currency='RUB')

    def __str__(self):
        return self.name

@register_model
class RoomType(models.Model):
    name = models.CharField('Наименование', max_length=100)
    image = models.ImageField('Изображение', blank=True, null=True)

    def __str__(self):
        return self.name

@register_model
class Room(models.Model):
    number = models.CharField('Номер', max_length=5)
    type = models.ForeignKey('RoomType', verbose_name='Тип номера', on_delete=models.CASCADE)
    max_occupancy = models.PositiveSmallIntegerField('Количество мест')
    price = MoneyField('Стоимость', max_digits=10, decimal_places=2, default_currency='RUB')

    def __str__(self):
        return self.number

@register_model
class Reservation(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateField('Дата въезда')
    check_out = models.DateField('Дата выезда')
    occupancy = models.PositiveSmallIntegerField('Вместимость')
    total_price = MoneyField('Стоимость', max_digits=10, decimal_places=2, default_currency='RUB')
    services = models.ManyToManyField('Service')

    def __str__(self):
        return self.name