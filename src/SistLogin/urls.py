from django.urls import path

from . import views

urlpatterns = [
    path('', views.menu, name='index'),
    path('login', views.login, name='login'),
    path('registro', views.index, name='registro'),
    path('logininvalido', views.login, name='login_invalido'),
    path('menu', views.menu, name='menu'),
]