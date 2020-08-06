from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.search_home),
    path('login/', views.search_login),
    path('signup/', views.search_signup),
    path('search/', views.search_list),
    path('content/<int:content_id>', views.show_content)
]
