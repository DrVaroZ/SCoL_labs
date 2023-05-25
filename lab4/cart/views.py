from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from car_rent.models import Car
from .cart import Cart
from .forms import CartAddCarForm
from django.core.exceptions import PermissionDenied


@require_POST
def cart_add(request, car_id):
    if not request.user.is_authenticated:
        raise PermissionDenied("No access")

    print('car id', car_id)
    cart = Cart(request)
    print(f'len:{len(cart)}')

    car = get_object_or_404(Car, id=car_id)
    if len(cart) >= 1:
        return redirect('cart:cart_detail')
    print(car.id)
    form = CartAddCarForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(car=car,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, car_id):
    if not request.user.is_authenticated:
        raise PermissionDenied("No access")

    cart = Cart(request)
    car = get_object_or_404(Car, id=car_id)
    cart.remove(car)
    return redirect('cart:cart_detail')


def cart_detail(request):
    if not request.user.is_authenticated:
        raise PermissionDenied("No access")

    cart = Cart(request)
    for tmp in cart:
        print(tmp)
    return render(request, 'cart/detail.html', {'cart': cart})
