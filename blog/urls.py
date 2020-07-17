from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('all/', views.all, name='all'),
    path('posts/<str:slug>/', views.detail, name='detail'),
    path('edit/<str:slug>/', views.edit, name='edit'),
    path('write/', views.write, name='write'),
]