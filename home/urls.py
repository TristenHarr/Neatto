from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

app_name = 'home'

urlpatterns = [
    #/home/
    url(r"^signup/$", views.UserFormView.as_view(), name='signup'),
    url(r"^login/$", auth_views.login, {'template_name': 'home/login.html'}, name='login'),
    url(r"^index/$", views.HomeView.as_view(), name='index'),
    url(r"^logout/$", auth_views.logout, {'next_page': '/home/login/'}, name='logout')
]