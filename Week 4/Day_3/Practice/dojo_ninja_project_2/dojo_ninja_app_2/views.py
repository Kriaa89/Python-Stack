from django.shortcuts import render, redirect
from . models import Dojo, Ninja

def index(request):
    dojos = Dojo.objects.all()
    return render(request, 'dojo_ninja_app_2/index.html', {'dojos': dojos})

def add_dojo(request):
    if request.method == "POST":
        Dojo.objects.create(
            name=request.POST['name'],
            city=request.POST['city'],
            state=request.POST['state'],
        )
    return redirect('/')

def add_ninja(request):
    if request.method == "POST":
        dojo = Dojo.objects.get(id=request.POST['dojo_id'])
        Ninja.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            dojo=dojo
        )
    return redirect('/')

def delete_dojo(request, dojo_id):
    dojo = Dojo.objects.get(id=dojo_id)
    dojo.delete()
    return redirect('/')