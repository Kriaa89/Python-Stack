from django.shortcuts import HttpResponse, redirect
from django.http import JsonResponse

# Redirect to "/blogs"
def root(request):
    return redirect('/blogs')

# Placeholder to display all blogs
def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

# Placeholder to display a new form for creating a blog
def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

# Redirect to "/"
def create(request):
    return redirect('/')

# Placeholder to display a specific blog by number
def show(request, number):
    return HttpResponse(f"placeholder to display blog number: {number}")

# Placeholder to edit a blog by number
def edit(request, number):
    return HttpResponse(f"placeholder to edit blog {number}")

# Redirect to "/blogs"
def destroy(request, number):
    return redirect('/blogs')

# Bonus: Return a JSON response
def json_response(request):
    return JsonResponse({"title": "My first blog", "content": "Lorem, ipsum dolor sit amet consectetur adipisicing elit."})

