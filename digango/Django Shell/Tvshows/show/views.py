from django.shortcuts import render,HttpResponse,redirect 
from . import models


def root(request):
    
    return redirect("/shows")

def show_new(request):
    context={
        'shows':models.get_all_show()
    }
    return render(request,"All_shows.html",context)

def add_new(request):
    return render(request,'add_show.html')



def creatshow(request):
    if request.method=="POST":
        models.create_show(request.POST)
        return redirect ('/shows')
    else:
        return HttpResponse('error')
    

    
def deleteshow(request,id):

    models.delete_show(id)
    return redirect ('/shows')




def getbyid(request,id):
    context = {
     'i': models.get_by_id(id)
    }
    return render (request,"read.html", context)




def edit(request,id):
    context ={
        'i':models.get_by_id(id)
    }
    return render (request,"update.html",context)


def confirm_uptade(request):
    if request.method=="POST":
        models.update_show(request.POST)
        return redirect('/')
    else:
        return HttpResponse("error")