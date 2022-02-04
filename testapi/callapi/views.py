from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import requests
def listuser(request):
     response= requests.get('http://localhost:8000/users/',{'username':'admin','password':'maram123'})
     print(response)
     return HttpResponse('call done')







