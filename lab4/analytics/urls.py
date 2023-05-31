from django.contrib import admin
from django.urls import path, include
#from django.conf import settings
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'analytics'

urlpatterns = [
    path('', views.show_analytics, name='show_analytics')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
