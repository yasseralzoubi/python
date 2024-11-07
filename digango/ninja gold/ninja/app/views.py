from django.shortcuts import render,HttpResponse,redirect 

# Create your views here.
#all of this Get request


def root(request):
    return render(request,"index.html")


# def process_money(request):
#     if request.method =="POST":
#         pass




#     else:
#         return redirect('/root')   



