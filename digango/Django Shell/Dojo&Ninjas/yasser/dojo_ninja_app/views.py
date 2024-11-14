from django.shortcuts import render,HttpResponse,redirect 
from . import models


def root(request):
    context={
        "dojos":models.get_Djos()
        }
    
    return render(request,"index.html",context)






def add_dojo(request):
    if request.method=="POST":
        models.create_Dojo(request.POST)
        return redirect('/')
    else:
        return HttpResponse("error")
    




def add_Ninja(request):
    if request.method=="POST":
        models.create_Ninja(request.POST)
        return redirect('/')
    else:
        return HttpResponse("error")
