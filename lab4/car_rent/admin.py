from django.contrib import admin
from .models import (Brand, CarModel, Car, Client, Rent, Advertisement,
                     CompanyPartner, Article, Company, NewsArticle, Question,
                     Worker, Vacancy, Review)


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
    # list_filter = ['discount', 'fines']


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'text', 'image', 'link']


@admin.register(CompanyPartner)
class CompanyPartnerAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'image', 'link']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['date', 'title', 'short', 'image']


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'info', 'logo', 'video_link',
                    'certificate', 'requisites', 'company_history']


@admin.register(NewsArticle)
class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'short', 'image', 'full_link']


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['date', 'question', 'answer']


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'phone_number', 'email', 'work_info']


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ['position', 'position_info', 'salary']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['date', 'author', 'mark', 'text']
