from django.urls import path
from . import views

app_name = 'homelink'

urlpatterns = [
    path('', views.class_spider, name='scrapy_index'),
]