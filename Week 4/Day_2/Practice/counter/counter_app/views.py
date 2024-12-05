from django.shortcuts import render, redirect

def index(request):
    if 'counter' not in request.session:
        request.session['counter'] == 0
    request.session['counter'] += 1
    if 'visiter' not in request.session:
        request.session['visiter'] == 0
    
    request.session['counter'] += 1
    request.session['visiter'] += 1

    return render(request, 'index.html')

def destroy_session_counter(request):
    # clear session and redirect to root
    if 'counter' in request.session:
        del request.session['counter']
    return redirect('/')

def destroy_session_visiter(request):
    # clear session and redirect to root
    if 'visiter' in request.session:
        del request.session['visiter']
        return redirect('/')

def increment(request, amount):
    if 'counter' in request.session:
        request.session['counter'] += amount
    return redirect('/')


