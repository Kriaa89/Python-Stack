from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('success', views.success, name='success'),
    path('logout', views.logout, name='logout'),
    path('check_email/', views.check_email, name='check_email'),
]