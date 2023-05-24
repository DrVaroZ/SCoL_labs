from django.shortcuts import render, get_object_or_404
from .models import Car, Brand, CarModel
from cart.forms import CartAddCarForm


def car_list(request, car_brand=None):
    brand = None
    brands = Brand.objects.all()
    cars = Car.objects.all()

    if car_brand:
        brand = get_object_or_404(Brand, name=car_brand)
        cars = cars.filter(brand=brand)
    return render(request,
                  'car_rent/car/list.html',
                  {'brand': brand,
                   'brands': brands,
                   'cars': cars})


def car_detail(request, id):
    car = get_object_or_404(Car, id=id)
    cart_car_form = CartAddCarForm()
    return render(request,
                  'car_rent/car/detail.html',
                  {'car': car, 'cart_car_form': cart_car_form})



