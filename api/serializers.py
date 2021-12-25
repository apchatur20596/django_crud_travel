from rest_framework import serializers
from .models import TravelPlans

class TravelPlansSerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelPlans
        fields = ['id', 'title', 'start', 'end', 'description', 'price']