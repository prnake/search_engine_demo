from django.urls import path, include
from django.conf.urls import url
from . import views


urlpatterns = [
    path('', views.search_home),
    url(r'^login/$', views.login,name="login"),
    url(r'^signup/$', views.signup,name="signup"),
    url(r'^search/$', views.search_list,name="search"),
    url(r'^logout/$', views.logout,name="logout"),
    path('content/<int:content_id>', views.show_content)
]
