from django.shortcuts import *
from datetime import *
# Create your views here.
def page(request):
    return redirect("/timedisplay") 

def timedisplay(request): 
    now = datetime.now()
    context = {
        'date_time': now.strftime("%b %d %Y %I:%M:%S %p"),
    }
    return render(request , "index.html" , context)