from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='Homepage.html'),
    path('traffic_admin/', views.admin, name='traffic_admin'),
    path('traffic_admin/login', views.login, name='login.html'),
    path('traffic_admin/registration', views.registration, name='registration.html'),
]