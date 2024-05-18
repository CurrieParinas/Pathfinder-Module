from django.shortcuts import render
from django.http import HttpResponse
from .models import Room

# Create your views here.
def home(request):
    context = {
        'rooms': Room.objects.all()
    }
    return render(request, 'wayfinderpro/home.html', context)