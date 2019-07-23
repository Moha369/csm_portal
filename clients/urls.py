from django.urls import path
from django.conf.urls import url, include
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name="clients-home"),
    path('client/<int:pk>/', PostDetailView.as_view(), name="post-detail"),
    path('client/new/', PostCreateView.as_view(), name="post-create"),
    path('client/<int:pk>/update/', PostUpdateView.as_view(), name="post-update"),
    path('client/<int:pk>/delete/', PostDeleteView.as_view(), name="post-delete"),
    path('about/', views.about, name="clients-about"),
]
