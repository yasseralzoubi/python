from django.shortcuts import render,HttpResponse,redirect 
from . import models


def root(request):
    context={
        "books":models.get_books()
        }
    return render(request,"index.html",context)


def add_book(request):
    if request.method=="POST":
        models.add_Book(request.POST)
        return redirect('/')
    else:
        return HttpResponse("Error")
    
    
def bookdesc(request,id):
    context={
    "book": models.get_book_id(id)
    }

    return render(request,"descriotion.html",context)


def author(request):
    context={
        "authors":models.get_authors()
        }
    return render(request,"add_author.html",context)




def add_author(request):
    if request.method=="POST":
        models.add_author(request.POST)
        return redirect('/author')
    else:
        return HttpResponse('error')
    

