from django.urls import path
from . import views



urlpatterns = [

        path('', views.index, name='index.html'),
        path('movies.html/', views.movies, name='movies.html'),
        path('shows.html/', views.shows, name='shows.html'),
        path('books.html/', views.books, name='books.html'),
        

]