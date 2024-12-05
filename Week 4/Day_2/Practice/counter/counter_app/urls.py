from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('destroy_session_counter', views.destroy_session_counter),
    path('destroy_session_visiter', views.destroy_session_visiter),
    path('increment', views.increment),
]