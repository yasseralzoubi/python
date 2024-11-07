from django.shortcuts import render,HttpResponse,redirect 

# Create your views here.
#all of this Get request
def root(request):
    context={
        'data': [
            {'first':'yasser','last':"alzoubi","age":"25"},
            {'first':'ali', 'last':'isa' , 'age':'30'},
            {'first':'khaled' , 'last' : 'nassar' , 'age' : '40'}, 
        ]
    }
    return render(request,"index.html",context)



