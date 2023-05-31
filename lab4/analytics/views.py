import os
from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from orders.models import Order, OrderItem
import matplotlib.pyplot as plt
from django.conf import settings
import numpy as np


def show_analytics(request):
    if not request.user.is_superuser:
        raise PermissionDenied("No access")

    pt = dict()

    x = []
    y = []

    for order in Order.objects.all():
        pt[str(order.created.year) + '.' + str(order.created.month) + '.' + str(order.created.day)] = 0

    for order in Order.objects.all():
        pt[str(order.created.year) + '.' + str(order.created.month) + '.' + str(order.created.day)] += 1

    for tmp in pt:
        x.append(tmp)
        y.append(pt[tmp])

    plt.xlabel('date', fontsize=10)
    plt.ylabel('order amount', fontsize=10)
    plt.plot(x, y)
    # plt.show()
    if request.method == "GET":
        plt.savefig(os.path.join(settings.MEDIA_ROOT, 'orders_per_day.png'), format='png')
        plt.close()

    amount_orders_per_day = list(pt.values())
    mean_orders_per_day = np.mean(amount_orders_per_day)
    median_orders_per_day = np.median(amount_orders_per_day)
    min_orders_per_day = np.min(amount_orders_per_day)
    max_orders_per_day = np.max(amount_orders_per_day)
    std_orders_per_day = np.std(amount_orders_per_day)

    return render(request,
                  'analytics/detail.html',
                  {'mean_orders_per_day': mean_orders_per_day,
                   'median_orders_per_day': median_orders_per_day,
                   'min_orders_per_day': min_orders_per_day,
                   'max_orders_per_day': max_orders_per_day,
                   'std_orders_per_day': std_orders_per_day})
