from django.shortcuts import render,HttpResponse,redirect 

# Create your views here.
#all of this Get request


def root(request):
    if 'visits' not in request.session:
        request.session['visits'] = 1
    else:
        request.session['visits'] += 1
    
    return render(request,"index.html")


def clears(request):
        request.session.flush()
    
        return redirect("jalal")

    
