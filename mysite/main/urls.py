from django.urls import path
from . import views

urlpatterns = [

        path('', views.index, name='index'),
        path('movies/', views.movies, name='movies'),
        path('shows/', views.shows, name='shows'),
        path('books/', views.books, name='books'),
        

]