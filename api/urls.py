from django.urls import path
from .views import travelplans_list
from .views import Index


urlpatterns = [
    path('', Index),
    path('travelplans/', travelplans_list),
]
