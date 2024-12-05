from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),  # Show all courses
    path('add', views.add_course, name="add_course"),  # Add a new course
    path('delete/<int:course_id>', views.delete_confirmation, name="delete_confirmation"),  # Confirm deletion
    path('delete/<int:course_id>/confirm', views.delete_course, name="delete_course"),  # Delete course
]
