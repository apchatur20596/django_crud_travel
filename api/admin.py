from django.contrib import admin
from .models import TravelPlans

# Register your models here.

@admin.register(TravelPlans)
class TravelPlansModel(admin.ModelAdmin):
    list_fiter = ('title', 'price')
    list_display = ('title', 'start', 'end', 'description', 'price')
