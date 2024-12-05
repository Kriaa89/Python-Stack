from django.shortcuts import render, redirect
import random

def index(request):
    if 'random_number' not in request.session:
        request.session['random_number'] = random.randint(1, 100)
        request.session['attempts'] = 0 
        request.session['game_over'] = False
    return render(request, 'index.html')

def guess(request):
    if 'attempts' not in request.session:
        request.session['attempts'] = 0
    if 'game_over' not in request.session:
        request.session['game_over'] = False
    if request.method == 'POST':
        user_guess = int(request.POST.get('guess'))
        request.session['attempts'] += 1
        
        if user_guess < request.session['random_number']:
            request.session['message'] = 'too low!'
        elif user_guess > request.session['random_number']:
            request.session['message'] = 'too high!'
        else:
            request.session['message'] = 'correct!'
            request.session['game_over'] = True
        if request.session['attempts'] >= 5 and not request.session['game_over']:
            request.session['message'] = "You lose! Try again."
            request.session['game_over'] = True
        
    return redirect('/')

def reset(request):
    if 'random_number' in request.session:
        del request.session['random_number']
    if 'attempts' in request.session:
        del request.session['attempts']
    if 'game_over' in request.session:
        del request.session['game_over']
    if 'message' in request.session:
        del request.session['message']
    return redirect('/')
