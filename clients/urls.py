from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="clients-home"),
    path('about/', views.about, name="clients-about"),
]
