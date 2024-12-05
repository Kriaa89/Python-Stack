from django.shortcuts import render, redirect
import random
from datetime import datetime

def index(request):
    # Initialize session variables if they don't exist
    if 'gold' not in request.session:
        request.session['gold'] = 0
        request.session['activities'] = []
        request.session['moves'] = 0
        request.session['goal'] = 0
        request.session['current_moves'] = 0
        request.session['message'] = ''
    return render(request, 'game/index.html')

def process_money(request, location):
    if request.method == 'POST':
        # Determine gold earned based on location
        if location == 'farm':
            gold_earned = random.randint(10, 20)
        elif location == 'cave':
            gold_earned = random.randint(5, 10)
        elif location == 'house':
            gold_earned = random.randint(2, 5)
        elif location == 'casino':
            gold_earned = random.randint(-50, 50)
        else:
            gold_earned = 0

        # Update session variables
        request.session['gold'] += gold_earned
        request.session['current_moves'] += 1
        activity = {
            'location': location,
            'gold': gold_earned,
            'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        request.session['activities'].append(activity)
        request.session.modified = True

        # Check win conditions
        if request.session['current_moves'] >= request.session['moves']:
            if request.session['gold'] >= request.session['goal']:
                request.session['message'] = "Congratulations! You've reached your goal!"
            else:
                request.session['message'] = "Game over! You didn't reach your goal."
            return redirect('/')

    return redirect('/')

def set_conditions(request):
    if request.method == 'POST':
        request.session['moves'] = int(request.POST['moves'])
        request.session['goal'] = int(request.POST['goal'])
        request.session['current_moves'] = 0
        request.session['message'] = ''
    return redirect('/')

def set_condition(request):
    if request.method == 'POST':
        request.session['moves'] = int(request.POST['moves'])
        request.session['goal'] = int(request.POST['goal'])
        request.session['message'] = None
        return redirect('/')
    return render(request, 'game/index.html')