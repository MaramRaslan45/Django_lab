# from django.shortcuts import
import json

from django.contrib.auth.models import User
from django.http import JsonResponse


from affairs.models import Trainee
from rest_framework import viewsets, status
from .serializers import Userser
from rest_framework.decorators import api_view, action
from rest_framework.response import Response

# Create your views here.

class UserView(viewsets.ModelViewSet):
    queryset = Trainee.objects.all()
    serializer_class = Userser

 #------------------- with Postman----------------------

@api_view(['PUT'],)
def updateapi(request,id):
    trainee = Trainee.objects.get(id=id)
    data = request.data
    serializer = Userser(trainee, data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        print(serializer.errors)
        return JsonResponse({'status': 'failed'})



@api_view(['DELETE'],)
def deleteapiview(request,id):
    trainee=Trainee.objects.filter(id=id)
    if trainee:
        trainee.delete()
        return JsonResponse({'status':'ok'})
    return JsonResponse(Userser.errors)
