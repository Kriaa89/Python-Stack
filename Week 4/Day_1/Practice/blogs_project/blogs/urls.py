from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),  # Redirect to "/blogs"
    path('blogs', views.index),  # Display a placeholder for blogs
    path('blogs/new', views.new),  # Placeholder for creating a new blog
    path('blogs/create', views.create),  # Redirect to "/"
    path('blogs/<int:number>', views.show),  # Display blog number
    path('blogs/<int:number>/edit', views.edit),  # Edit blog number
    path('blogs/<int:number>/delete', views.destroy),  # Redirect to "/blogs"
    path('blogs/json', views.json_response),  # Bonus: Return JSON
]