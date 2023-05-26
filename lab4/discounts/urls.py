from . import views
from django.urls import path

app_name = 'discounts'

urlpatterns = [
    path('apply/', views.discount_apply, name='apply'),
]