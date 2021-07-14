from django.http import HttpResponse
from django.shortcuts import render

def jumppage(request):
    return render(request,"main.html")