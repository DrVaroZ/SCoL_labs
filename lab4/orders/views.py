from django.shortcuts import render
from .models import OrderItem
# from .forms import OrderCreateForm
from cart.cart import Cart
from car_rent.models import Client
from .models import Order
from django.core.exceptions import PermissionDenied
from discounts.models import Discount


def order_create(request):
    if not request.user.is_authenticated:
        raise PermissionDenied("No access")

    cart = Cart(request)
    if request.method == 'POST':
        order = Order.objects.create(client=Client.objects.filter(email=request.user.email).first(),
                                     discount=cart.discount,
                                     discount_percentage=cart.discount.discount)
        print(Client.objects.all())
        print(request.user.email)

        for item in cart:
            OrderItem.objects.create(order=order,
                                     car=item['car'],
                                     price=item['rent_per_day'],
                                     quantity=item['quantity'],
                                     total_cost=cart.get_total_price_after_discount())

        # cleaning cart
        cart.clear()
        return render(request, 'order/created.html',
                      {'order': order})

    return render(request, 'order/create.html',
                  {'cart': cart})
