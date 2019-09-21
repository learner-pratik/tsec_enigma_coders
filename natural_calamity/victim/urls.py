from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='main'),
    path('addvolunteer/', views.login, name='admin'),
    #path('victim/', views.login, name='victim'),
    path('vsignup',views.addVolunteer, name='volunteersignup'),
    path('vollogin',views.volunteerlogin, name='volunteerlogin'),
    path('vologin',views.volunteerreg, name='vol_register'),
    path('volunteer',views.Templogin, name='volunteer'),
    path('admin_panel',views.AdminLogin,name="admin")
]