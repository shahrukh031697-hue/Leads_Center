

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('contact/', views.contact, name='contact'),
    path(
        'principal-message/',
        views.principal_message,
        name='principal_message'
    ),
path(
        'caprogram/',
        views.caprogram(),
        name='principal_message'
    ),
path(
        'accaprogram/',
        views.accaprogram(),
        name='accaprogram'
    ),
]