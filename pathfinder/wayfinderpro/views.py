from django.shortcuts import render
from django.http import HttpResponse
from django.core.serializers import serialize
from .models import Room

# Create your views here.
def home(request):
    rooms = Room.objects.all()
    context = {
        'rooms': rooms,
        'rooms_json': serialize('json', rooms)
    }
    return render(request, 'wayfinderpro/initial.html', context)

# Add error checking 
def finder(request):
    if request.method == 'POST':
        selected_room_slug = request.POST['room_selection']

        try:
            selected_room = Room.objects.get(slug=selected_room_slug)
        except Room.DoesNotExist:
            return HttpResponse("Room not found")
        print(selected_room)
        context = {
        'rooms': Room.objects.all(),
        'selectedRoom': selected_room,
        }
        return render(request, 'wayfinderpro/finder.html', context)
    else:
        context = {
        'rooms': Room.objects.all()
        }
        return render(request, 'wayfinderpro/finder.html', context)

def get_room_coordinates(request, slug):
    try:
        currentRoom = Room.objects.get(slug=slug)
    except Room.DoesNotExist:
        return HttpResponse("Room not found")

    print(currentRoom.x, currentRoom.y, currentRoom.floor)

    context = {
        'x' : currentRoom.x,
        'y' : currentRoom.y,
        'floorNumber' : currentRoom.floor
    }
    return render(request, 'wayfinderpro/initial.html', context)

# def get_all_RH_rooms(request):
#     building = Building.objects.get(slug='rizal-hall')
#     rooms = Room.objects.filter(building=building).order_by('name')
#     print(rooms)

#     context = {
#         'rooms': rooms
#     }
#     return render(request,'pathfinder.html', context)