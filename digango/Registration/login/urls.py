from django.urls import path     
from . import views
urlpatterns = [
    path('', views.root),   
    path('success' , views.success),
    path('regestraion' , views.regestration),
    path('login' , views.login),
    path('logout' , views.logout) ,
    

]