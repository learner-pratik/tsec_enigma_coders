from django.urls import path
from . import views

urlpatterns = [
    path('victim/', views.login, name='victim'),
]