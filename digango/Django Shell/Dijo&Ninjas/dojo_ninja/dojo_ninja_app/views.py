from django.shortcuts import render,HttpResponse,redirect 
from . import models


def root(request):
    
    return render(request,"index.html")
