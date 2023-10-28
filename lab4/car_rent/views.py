import re
from docx import Document
import requests
from django.shortcuts import render, get_object_or_404

from login.models import CustomUser
from .models import (Car, Brand, CarModel, Advertisement, CompanyPartner, Article,
                     Company, NewsArticle, Question, Worker, Vacancy, Review)
from discounts.models import Discount
from cart.forms import CartAddCarForm
from .forms import CarForm, ReviewForm
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from django.core.exceptions import PermissionDenied
from datetime import date


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

    # print(12345)

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


def show_home_page(request):
    advertisements = Advertisement.objects.all()
    companies = CompanyPartner.objects.all()
    article = Article.objects.last()
    return render(request,
                  'car_rent/info_pages/home.html',
                  {'advertisements': advertisements,
                   'companies': companies,
                   'article': article})


def show_about_company_page(request):
    company_info = Company.objects.last()
    return render(request,
                  'car_rent/info_pages/about_company.html',
                  {'company_info': company_info})


def show_news_page(request):
    news = NewsArticle.objects.all()
    return render(request,
                  'car_rent/info_pages/news.html',
                  {'news': news})


def show_faq_page(request):
    questions = Question.objects.all()
    return render(request,
                  'car_rent/info_pages/faq.html',
                  {'questions': questions})


def show_contacts_page(request):
    workers = Worker.objects.all()
    return render(request,
                  'car_rent/info_pages/contacts.html',
                  {'workers': workers})


def show_privacy_policy_page(request):
    doc = Document("../lab4/media/privacy.docx")
    html_code = ""
    for paragraph in doc.paragraphs:
        paragraph_html = paragraph.text.replace('\n', '<br>')
        html_code += f"<p>{paragraph_html}</p>"
    return render(request,
                  'car_rent/info_pages/privacy_policy.html',
                  {'privacy': html_code})


def show_vacancies_page(request):
    vacancies = Vacancy.objects.all()
    return render(request,
                  'car_rent/info_pages/vacancies.html',
                  {'vacancies': vacancies})


def create_review(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect("/auth/login/")

    form = ReviewForm()

    for obj in CustomUser.objects.all():
        print(obj.id)

    if request.method == "POST":
        print('id', request.user.id)
        review = Review.objects.create(date=date.today().strftime('%Y-%m-%d'),
                                       author=CustomUser.objects.get(id=request.user.id),
                                       mark=request.POST.get('mark'),
                                       text=request.POST.get('text'))

        review.save()
    else:
        return render(request, "car_rent/info_pages/review_create.html", {"form": form})
    return HttpResponseRedirect("/")


def show_reviews_page(request):
    reviews = Review.objects.all()
    return render(request,
                  'car_rent/info_pages/reviews.html',
                  {'reviews': reviews})


def show_discounts_page(request):
    active_discounts = Discount.objects.filter(active=True)
    expired_discounts = Discount.objects.filter(active=False)
    return render(request,
                  'car_rent/info_pages/discounts.html',
                  {'active_discounts': active_discounts,
                   'expired_discounts': expired_discounts})


def show_experiments_page(request):
    return render(request,
                  'car_rent/info_pages/experiments.html')


def show_js_sandbox_page(request):
    return render(request,
                  'car_rent/info_pages/js_sandbox.html')
