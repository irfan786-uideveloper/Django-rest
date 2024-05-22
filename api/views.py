from django.shortcuts import render

from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Person
from .serializers import PersonSerializer
from rest_framework import status

from django.shortcuts import get_object_or_404

# Create your views here.

@api_view(['GET'])
def getData(request):
  persondata=Person.objects.all()
  serializer=PersonSerializer(persondata,many=True)
  return Response(serializer.data)

@api_view(['POST'])
def createData(request):
  serializer=PersonSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
  return Response(serializer.data)

@api_view(['POST'])
def UpdateData(request,id):
  person=Person.objects.get(id=id)
  serializer=PersonSerializer(instance=person,data=request.data)
  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data)
  else:
    return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def DeleteData(request,id):
  person=get_object_or_404(Person,id=id)
  person.delete()
  return Response(status=status.HTTP_202_ACCEPTED)