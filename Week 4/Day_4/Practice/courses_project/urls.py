
from django.contrib import admin
from django.urls import path, include
from courses import views  # Make sure to import views from the courses app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('courses/', include('courses.urls')),
    path('shows/', views.shows, name='shows'),
]