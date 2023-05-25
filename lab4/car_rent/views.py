import requests
from django.shortcuts import render, get_object_or_404
from .models import Car, Brand, CarModel
from cart.forms import CartAddCarForm
from .forms import CarForm
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from django.core.exceptions import PermissionDenied


def car_list(request, car_brand=None):
    brand = None
    brands = Brand.objects.all()
    cars = Car.objects.all()
    sort_type = request.GET.get('sort')

    if str(sort_type) == 'ascending':
        cars = cars.order_by('rent_per_day')
    elif str(sort_type) == 'descending':
        cars = cars.order_by('-rent_per_day')

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

    joke = requests.get('https://official-joke-api.appspot.com/jokes/programming/random').json()[0]

    return render(request,
                  'car_rent/car/detail.html',
                  {'car': car, 'cart_car_form': cart_car_form,
                   'joke': joke['setup'] + joke['punchline']})


def car_create(request):
    if not request.user.is_staff:
        raise PermissionDenied("No access")

    print(1234567)

    form = CarForm()

    if request.method == "POST":
        car = Car.objects.create(brand=Brand.objects.get(id=request.POST.get('brand')),
                                 car_model=CarModel.objects.get(id=request.POST.get('car_model')),
                                 release_year=request.POST.get('release_year'),
                                 cost=request.POST.get('cost'),
                                 rent_per_day=request.POST.get('rent_per_day'),
                                 image=request.FILES.get('image'))

        car.save()
    else:
        return render(request, "car_rent/car/create.html", {"form": form})
    return HttpResponseRedirect("/")


# editing data in database
def car_edit(request, id):
    if not request.user.is_staff:
        raise PermissionDenied("No access")

    try:
        car = Car.objects.get(id=id)

        form = CarForm(initial={'brand': car.brand, 'car_model': car.car_model,
                                'release_year': car.release_year, 'cost': car.cost,
                                'rent_per_day': car.rent_per_day, 'image': car.image})

        if request.method == "POST":
            car.brand = Brand.objects.get(id=request.POST.get('brand'))
            car.car_model = CarModel.objects.get(id=request.POST.get('car_model'))
            car.release_year = request.POST.get('release_year')
            car.cost = request.POST.get('cost')
            car.rent_per_day = request.POST.get('rent_per_day')
            car.image = request.FILES.get('image')

            car.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "car_rent/car/edit.html", {"car": car, 'form': form})
    except car.DoesNotExist:
        return HttpResponseNotFound("<h2>car not found</h2>")


# removing data from databasse
def car_delete(request, id):
    if not request.user.is_staff:
        raise PermissionDenied("No access")

    try:
        car = Car.objects.get(id=id)
        car.delete()
        return HttpResponseRedirect("/")
    except car.DoesNotExist:
        return HttpResponseNotFound("<h2>car not found</h2>")
