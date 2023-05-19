from django.contrib import admin
from .models import Brand, CarModel, Car, CarInstance, Discount, Fine, Client


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    pass


@admin.register(CarInstance)
class CarInstanceAdmin(admin.ModelAdmin):
    pass


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    pass


@admin.register(Fine)
class FineAdmin(admin.ModelAdmin):
    pass


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    pass
