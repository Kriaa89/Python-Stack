
from django.urls import path
from django.urls import path
from . import views

urlpatterns = [
    path('', views.redirect_to_show),
    path('shows', views.show_index, name='show_index'),
    path('shows/new', views.new_show, name='new_show'),
    path('shows/create', views.create_show, name='create_show'),
    path('shows/<int:id>', views.show_detail, name='show_detail'),
    path('shows/<int:id>/edit', views.edit_show, name='edit_show'),
    path('shows/<int:id>/update', views.update_show, name='update_show'),
    path('shows/<int:id>/destroy', views.destroy_show, name='destroy_show'),
]