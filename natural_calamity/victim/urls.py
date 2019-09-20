from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='main'),
    path('addvolunteer/', views.login, name='admin'),
    #path('victim/', views.login, name='victim'),
    path('vsignup',views.addVolunteer,name='volunteersignup'),
]