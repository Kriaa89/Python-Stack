from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('process_money/<str:location>', views.process_money),
    path('set_conditions', views.set_condition),

]