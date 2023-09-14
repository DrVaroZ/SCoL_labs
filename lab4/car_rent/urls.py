from django.urls import path
from . import views


app_name = 'car_rent'

urlpatterns = [
    path('', views.car_list, name='car_list'),
    path("create/", views.car_create),
    path("edit/<int:id>/", views.car_edit),
    path("delete/<int:id>/", views.car_delete),
    path("home/", views.show_home_page, name='home'),
    path("about_company/", views.show_about_company_page, name='about_company'),
    path("news/", views.show_news_page, name='news'),
    path("faq/", views.show_faq_page, name='faq'),
    path("contacts/", views.show_contacts_page, name='contacts'),
    path("privacy_policy/", views.show_privacy_policy_page, name='privacy_policy'),
    path("vacancies/", views.show_vacancies_page, name='vacancies'),
    path("reviews/", views.show_reviews_page, name='reviews'),
    path('reviews/create/', views.create_review),
    path("discounts/", views.show_discounts_page, name='discounts'),
    path('<str:car_brand>/', views.car_list,
         name='car_list_by_brand'
         ),
    path('<int:id>', views.car_detail,
         name='car_detail'),
]
