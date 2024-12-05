from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Course, Description

# Root route to display courses
def index(request):
    context = {
        "courses": Course.objects.all()
    }
    return render(request, "shows.html", context)

# Add a new course
def add_course(request):
    if request.method == 'GET':
        return render(request, 'add_course.html')
    if request.method == "POST":
        # Validate the data
        errors = Course.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        
        # Create the course
        new_course = Course.objects.create(name=request.POST['name'])
        # Ninja Bonus: Create the description
        if 'description' in request.POST and request.POST['description']:
            description = Description.objects.create(content=request.POST['description'])
            new_course.description = description
            new_course.save()

        return redirect('/')

# Render the confirmation page for deleting a course
def delete_confirmation(request, course_id):
    course = Course.objects.get(id=course_id)
    context = {
        "course": course,
        "description": course.description.content if course.description else "No Description"
    }
    return render(request, "delete.html", context)

# Delete a course
def delete_course(request, course_id):
    if request.method == "POST":
        course = Course.objects.get(id=course_id)
        course.delete()
        return redirect('/')

