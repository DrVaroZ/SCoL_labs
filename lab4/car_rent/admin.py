from django.contrib import admin
from .models import Brand, CarModel, Car, Client, Rent


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['brand', 'car_model', 'release_year', 'cost', 'rent_per_day', 'image']
    list_filter = ['brand', 'car_model']


@admin.register(Rent)
class RentAdmin(admin.ModelAdmin):
    list_display = ['car', 'client', 'start_date', 'finish_date', 'amount_of_rent_days', 'rent_cost',
                    'discount_sum', 'fine_sum', 'result_sum', 'status']
    list_filter = ['finish_date']


'''
@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ['name', 'percentage']


@admin.register(Fine)
class FineAdmin(admin.ModelAdmin):
    list_display = ['name', 'sum_fine']

'''

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'date_birthday', 'email', 'phone_number']
    #list_filter = ['discount', 'fines']
