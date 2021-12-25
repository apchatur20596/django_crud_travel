from django.shortcuts import render, HttpResponse
from .models import TravelPlans
from .serializers import TravelPlansSerializer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

def Index(request):
    return HttpResponse("It is working")

@api_view(['GET', 'POST'])
def travelplans_list(request):

    #get all travel plans
    if request.method == 'GET':
        travelplans = TravelPlans.objects.all()
        serializer = TravelPlansSerializer(travelplans, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TravelPlansSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)   

@api_view(['GET', 'PUT', 'DELETE'])
def travelplans_details(request, pk):
    try:
        travelplan = TravelPlans.objects.get(pk=pk)

    except TravelPlans.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TravelPlansSerializer(travelplan)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TravelPlansSerializer(travelplan, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        travelplan.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)