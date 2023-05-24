from django.shortcuts import render
from .models import OrderItem
# from .forms import OrderCreateForm
from cart.cart import Cart
from car_rent.models import Client
from .models import Order
from django.core.exceptions import PermissionDenied


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        order = Order.objects.create(client=Client.objects.filter(email=request.user.email).first())

        for item in cart:
            OrderItem.objects.create(order=order,
                                     car=item['car'],
                                     price=item['rent_per_day'],
                                     quantity=item['quantity'])

        # cleaning cart
        cart.clear()
        return render(request, 'order/created.html',
                      {'order': order})

    return render(request, 'order/create.html',
                  {'cart': cart})
