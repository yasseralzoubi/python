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
    "book": models.get_book_id(id),
    "authors":models.get_authors(),
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
        return redirect('/authors')
    else:
        return HttpResponse('error')
    

def get_author(request,id):
    print(models.get_author_id(id).books.all())
    context={
    "author": models.get_author_id(id),
    "books": models.get_books(),
    "author_books":models.get_author_id(id).books.all()
    }

    return render(request,"notes.html",context)


def displaybook(request,id):
    book_id=request.POST.get('book_id')
    book = models.get_book_id(book_id)
    author=models.get_author_id(int(id))
    author.books.add(book)

    print(book)
    return redirect(f'/author/{id}')

def displayauthor(request,id):
    author_id=request.POST['authors_id']
    print("#######################")
    print(author_id)
    book = models.get_book_id(id)
    author=models.get_author_id(int(author_id))
    book.authors.add(author)
    print(book)
    
    return redirect(f'/bookdesc/{id}')




    

