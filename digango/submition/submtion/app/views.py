from django.shortcuts import render,HttpResponse,redirect 

# Create your views here.
#all of this Get request
def root(request):
    return render(request,"information.html")

def submtion(request):
    print("test")
    name=request.POST['your_name']
    location=request.POST['Location']
    lan=request.POST['language']
    conmment=request.POST['comment']

    context = {
        "name" : name,
        "location" : location,
        "lan" : lan,
        "conmment" : conmment,
    }
    
    return render(request,"submtion.html",context)