from django.urls import path
from . import views

app_name = 'info'

urlpatterns = [
    path('', views.index, name='home'),
    path('resume/', views.resume, name='resume'),
]