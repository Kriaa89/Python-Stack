from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from .models import User
import bcrypt

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == "POST":
        errors = User.objects.validate_registration(request.POST)
        if errors:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        
        # hash password
        pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()

        # create user 
        user = User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            password = pw_hash,
            birthday = request.POST['birthday']
        )
        # store user id in session
        request.session['user_id'] = user.id
        messages.success(request, "User successfully created")
        return redirect('/success')
    return redirect('/')

def login(request):
    if request.method == "POST":
        errors = User.objects.validate_login(request.POST)
        if errors:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        user = User.objects.get(email=request.POST['email'])
        request.session['user_id'] = user.id
        messages.success(request, "Successfully logged in!")
        return redirect('/success')
    return redirect('/')

def success(request):
    if 'user_id' not in request.session:
        messages.error(request, "Please log in first!")
        return redirect('/')
    context = {
        'user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'login_app/success.html', context)

def logout(request):
    request.session.flush()
    return redirect('/')

def check_email(request):
    email = request.GET.get('email', None)
    data = {
        'is_taken': User.objects.filter(email=email).exists()
    }
    return JsonResponse(data)
