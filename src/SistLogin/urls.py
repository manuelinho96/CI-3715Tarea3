from django.urls import path

from . import views

urlpatterns = [
    path('', views.menu, name="menu"), # Ruta del index   
    path('menu', views.menu, name='menu'), # Ruta del menu.
    path('login', views.login, name='login'), # Ruta del login
    path('registro', views.registro, name='registro'), # Ruta del registro
]