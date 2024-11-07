from django.shortcuts import render ,HttpResponse ,redirect

# Create your views here.
def index(request):


    return HttpResponse('placeholder to display a list of all blogs')


def create(request):

    return HttpResponse('route with a method called "create.')

def show(request,number):

    return HttpResponse(f"placeholder to display blog number: {number}")
# anything come from HTML come as str , i should convert it
# to add number you should convert number from str to int

def edit(request,number):

    return HttpResponse(f"placeholder to edit blog {number}")

def destroy(request,number):

    return redirect ("/blogs")