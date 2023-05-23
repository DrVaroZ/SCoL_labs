from django.urls import path
from . import views


app_name = 'car_rent'

urlpatterns = [
    path('', views.car_list, name='car_list'),
    path('<str:car_brand>/', views.car_list,
         name='car_list_by_brand'
         ),
    path('<int:id>', views.car_detail,
         name='car_detail'),
]
