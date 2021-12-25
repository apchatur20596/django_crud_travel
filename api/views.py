from django.shortcuts import render, HttpResponse
from .models import TravelPlans
from .serializers import TravelPlansSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser

# Create your views here.

def Index(request):
    return HttpResponse("It is working")

def travelplans_list(request):

    #get all travel plans
    if request.method == 'GET':
        travelplans = TravelPlans.objects.all()
        serializer = TravelPlansSerializer(travelplans, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TravelPlansSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        return JsonResponse(serializer.errors, status = 400)    