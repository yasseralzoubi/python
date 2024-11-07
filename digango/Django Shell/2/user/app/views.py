from django.shortcuts import render,HttpResponse,redirect 

# Create your views here.
#all of this Get request
def root(request):
    return HttpResponse("hello")