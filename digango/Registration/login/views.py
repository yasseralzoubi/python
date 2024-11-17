from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from . import models

# Create your views here.
def root(request):
    return render(request, "login.html")

def success(request):
    # التحقق من وجود المستخدم في الجلسة
    user_id = request.session.get('user_id')
    if user_id:
        # الحصول على بيانات المستخدم من قاعدة البيانات
        user = models.Registration.objects.get(id=user_id)
        return render(request, "success.html", {"first_name": user.firstname, "last_name": user.lastname})
    else:
        return render(request, "success.html")




def regestration(request):
    if request.method=="POST":
                # التحقق من البيانات المدخلة باستخدام basic_validator
        errors = models.Registration.objects.basic_validator(request.POST)
        if errors:
            return render(request, "login.html", {"errors": errors})
     
        user = models.insert_new_user_DB( request.POST )
        request.session['user_id'] =user.id
        return redirect ('/success')
    else:
        return HttpResponse('error')
    


def login(request):
    if request.method=="POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        if  models.authenticate_user(email,password):
            user= models.Registration.objects.get(email=email)

            request.session['user_id'] =user.id
            return redirect ('/success')
            

        
        else:
            messages.error(request ,"Invalid email or password")
            return redirect('/')
        


def logout(request):
    request.session.clear()
    return redirect('/')
            
    
    









        

        
