from unittest import result
from urllib import response
from django.http import HttpResponse
from django.shortcuts import render
from .models import destination


def index(request):
    
    desti = destination.objects.all()
    return render(request, 'index.html', {'desti': desti})