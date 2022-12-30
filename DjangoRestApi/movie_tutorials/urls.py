from django.urls import path
from movie_tutorials import views 

urlpatterns = [ 
    path('', views.movie_tutorials_list),

]