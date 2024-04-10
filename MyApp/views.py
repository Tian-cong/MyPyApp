from django.shortcuts import render
from django.http import HttpResponse

def dog(request):
    return render(request,"dog.html")