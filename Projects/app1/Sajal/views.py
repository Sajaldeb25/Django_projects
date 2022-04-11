from unittest import result
from urllib import response
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'home.html', {'name': 'Sajal'})

def add(request):
    var1 = request.POST["num1"]
    var2 = request.POST["num2"]

    res = int(var1) + int (var2)

    return render(request, 'result.html', {'result':res})