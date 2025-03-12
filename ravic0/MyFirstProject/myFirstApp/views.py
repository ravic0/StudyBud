from django.shortcuts import render
from .models import Room

# Create your views here.

def home(request):    
    rooms = Room.objects.all()
    context = {'rooms':rooms}
    return render(request, 'myFirstApp/home.html', context)

def room(request, value):
    room = Room.objects.get(id=int(value))
    context = {'room':room}
    return render(request, 'myFirstApp/room.html', context)
