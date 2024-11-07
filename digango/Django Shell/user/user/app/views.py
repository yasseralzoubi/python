from django.shortcuts import render,HttpResponse,redirect 
from . import models

# Create your views here.
#all of this Get request
def root(request):
    
    context={
        "user":models.get_user()
    }
    return render(request,"index.html",context)


def add_user(request):
    if request.method=="POST":
        models.create_user(request.POST)
        return redirect('/')
    else:
        return HttpResponse("error")

def delete(request,id):
    models.deleteuser(id)
    return redirect ('/')