from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.utils import timezone
from .models import Discount
from .forms import DiscountApplyForm


@require_POST
def discount_apply(request):
    now = timezone.now()
    form = DiscountApplyForm(request.POST)
    if form.is_valid():
        code = form.cleaned_data['code']

        all_discounts = Discount.objects.all()
        codes_all = []
        for disc in all_discounts:
            codes_all.append(disc.code)

        if code not in codes_all:
            code = 'no_discount'

        if Discount.objects.get(code=code,
                                valid_from__lte=now,
                                valid_to__gte=now,
                                active=True):
            discount = Discount.objects.get(code=code,
                                            valid_from__lte=now,
                                            valid_to__gte=now,
                                            active=True)
            request.session['discount_id'] = discount.id
        else:
            discount = Discount.objects.get(code__iexact='no_discount',
                                            valid_from__lte=now,
                                            valid_to__gte=now,
                                            active=True)
            request.session['discount_id'] = discount.id
        '''
                try:
            discount = Discount.objects.get(code__iexact=code,
                                            valid_from__lte=now,
                                            valid_to__gte=now,
                                            active=True)
            request.session['discount_id'] = discount.id
        except discount.DoesNotExist:
            discount = Discount.objects.get(code__iexact='no_discount',
                                            valid_from__lte=now,
                                            valid_to__gte=now,
                                            active=True)
            request.session['discount_id'] = discount.id
        '''

    return redirect('cart:cart_detail')
