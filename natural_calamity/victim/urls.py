from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='main'),
    path('victim/', views.login, name='victim'),
]