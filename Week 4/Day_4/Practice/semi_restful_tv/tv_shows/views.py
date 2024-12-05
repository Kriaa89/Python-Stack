from django.shortcuts import render, redirect 
from .models import Show
from datetime import datetime

def redirect_to_show(request):
    return redirect('/shows')

def show_index(request):
    shows = Show.objects.all()
    return render(request, 'tv_shows/index.html', {'shows': shows})

def new_show(request):
    return render(request, 'tv_shows/new.html')

def create_show(request):
    if request.method == "POST":
        try:
            release_date = datetime.strptime(request.POST['release_date'], '%Y-%m-%d').date()
        except ValueError:
            return redirect('/shows/new')
        
        new_show = Show.objects.create(
            title=request.POST['title'],
            network=request.POST['network'],
            release_date=release_date,
            description=request.POST['description'],
        )
        return redirect(f"/shows/{new_show.id}")
    return redirect('/shows')

def show_detail(request, id):
    show = Show.objects.filter(id=id)
    if not show.exists():
        return redirect('/shows')
    return render(request, 'tv_shows/show.html', {'show': show.first()})

def edit_show(request, id):
    show = Show.objects.filter(id=id)
    if not show.exists():
        return redirect('/shows')
    return render(request, 'tv_shows/edit.html', {'show': show.first()})

def update_show(request, id):
    if request.method == "POST":
        show = Show.objects.filter(id=id)
        if not show.exists():
            return redirect('/shows')
        
        show = show.first()
        try:
            release_date = datetime.strptime(request.POST['release_date'], '%Y-%m-%d').date()
        except ValueError:
            return redirect(f"/shows/{id}/edit")
        
        show.title = request.POST['title']
        show.network = request.POST['network']
        show.release_date = release_date
        show.description = request.POST['description']
        show.save()
    return redirect(f"/shows/{id}")

def destroy_show(request, id):
    show = Show.objects.filter(id=id)
    if show.exists():
        show.first().delete()
    return redirect('/shows')
