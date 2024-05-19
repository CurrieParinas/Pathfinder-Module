from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='wayfinderpro-home'),
    path('finder/', views.finder, name='wayfinderpro-room-finder'),
    path('finder/displayPath/', views.displayPath, name='wayfinderpro-display-path'),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)