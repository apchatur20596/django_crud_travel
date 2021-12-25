from django.urls import path
from .views import travelplans_list, travelplans_details
from .views import Index


urlpatterns = [
    path('', Index),
    path('travelplans/', travelplans_list),
    path('travelplans/<int:pk>/', travelplans_details)
]
