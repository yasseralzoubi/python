from django.shortcuts import render,HttpResponse,redirect 
import random

# Create your views here.
#all of this Get request
def root(request):
    if 'rand_num' not in request.session:                  #if it is empty
        request.session['rand_num']=random.randint(1,100)  # this will guss number betwween 1.100 and save it in session
    # print(request.session['rand_num'])
    return render(request,"index.html")                          


def process(request):
    
    guess = int(request.POST['guess'])               # it is related to input 
# always when i have session i activat imigrate 
    ran_num = request.session['rand_num'] 

    if(guess > ran_num):
        request.session['message'] ="too high"

    elif(guess<ran_num):
        request.session['message']="too low"

    else:
        request.session['message']= f"{guess}Was the number"
    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')