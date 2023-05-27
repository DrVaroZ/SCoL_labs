from django.db import models
from car_rent.models import Car, Client
from decimal import Decimal
from django.core.validators import MinValueValidator, MaxValueValidator
from discounts.models import Discount


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True)
    discount = models.ForeignKey(Discount,
                                 related_name='orders',
                                 on_delete=models.CASCADE,
                                 null=True,
                                 blank=True)
    discount_percentage = models.IntegerField(default=0,
                                              validators=[MinValueValidator(0),
                                                          MaxValueValidator(100)])

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        total_cost = sum(item.get_cost() for item in self.items.all())
        return total_cost - total_cost * (self.discount_percentage / Decimal('100'))


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    car = models.ForeignKey(Car, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
