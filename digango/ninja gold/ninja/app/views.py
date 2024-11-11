from django.shortcuts import render,HttpResponse,redirect 
import random

# Create your views here.
#all of this Get request


def root(request):
    if 'gold' not in request.session:
        request.session['gold']=0
        request.session['activites']=[]
    return render(request,"index.html")


def process_money(request):
    new_gold=random.randint(int(request.POST["min-gold"]),int(request.POST["max-gold"]))
    request.session['gold']+=new_gold
    place=request.POST["place"]
    if(new_gold>0):
        activity = f"Earned {new_gold} gold from {place}"

    else:
        activity = f"lost {new_gold} gold from {place}"
    request.session['activites'].append(activity)
    return redirect('/')



def reset(request):
    request.session.clear()
    return redirect('/')





        





