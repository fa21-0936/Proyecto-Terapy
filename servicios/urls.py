from django.urls import path
from . import views

urlpatterns = [
    path('', views.paginaInicio, name='paginaInicio'),
    path('servicios/', views.Servicios, name='Servicios'),
    path('privacidad/', views.privacidad, name='privacidad'),
    path('contacto/', views.contacto, name='contacto'),
    path('noticias/', views.noticias, name='noticias_list'),
    path('login/', views.custom_login, name='login_page'),
    path('logout/', views.custom_logout, name='logout_page'),
    path('reservar-servicio/', views.reservar_servicio, name='reservar_servicio'),
]