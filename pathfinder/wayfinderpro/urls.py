from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='wayfinderpro-home'),
    path('finder/', views.finder, name='wayfinderpro-room-finder'),
    path('getFloors/<str:college>/<str:building>/', views.get_floors, name='get_floors'),
    path('getRooms/<str:college>/<str:building>/', views.get_rooms, name='get_rooms'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)