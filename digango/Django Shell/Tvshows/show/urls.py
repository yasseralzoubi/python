from django.urls import path
from . import views    # the . indicates that the views file can be found in the same directory as this file
                    
urlpatterns = [
    path('', views.root),
    path('shows',views.show_new),
    path('shows/new',views.add_new),
    path('shows/creat',views.creatshow),
    path('shows/<int:id>/destroy',views.deleteshow),
    path('shows/<int:id>',views.getbyid),
    path('shows/<int:id>/edit',views.edit),
    path('confirm_update',views.confirm_uptade)

]