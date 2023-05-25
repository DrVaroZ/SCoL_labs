from django.urls import path
from . import views


app_name = 'car_rent'

urlpatterns = [
    path('', views.car_list, name='car_list'),
    path("create/", views.car_create),
    path("edit/<int:id>/", views.car_edit),
    path("delete/<int:id>/", views.car_delete),
    path('<str:car_brand>/', views.car_list,
         name='car_list_by_brand'
         ),
    path('<int:id>', views.car_detail,
         name='car_detail'),
]
