from django.urls import path
from . import views    # the . indicates that the views file can be found in the same directory as this file
                    
urlpatterns = [
    path('', views.root),
    path('Add_book',views.add_book),
    path('bookdesc/<int:id>',views.bookdesc,name='bookdesc'),
    path('author/<int:id>',views.author),
    path('add_author',views.add_author),
]