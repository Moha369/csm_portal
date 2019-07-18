from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
    path('', views.home, name="clients-home"),
    path('about/', views.about, name="clients-about"),
    path('links/', views.links, name="clients-links"),
]
