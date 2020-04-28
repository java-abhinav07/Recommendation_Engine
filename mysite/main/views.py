from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Movie, Book, TVShow
import random
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.core.serializers import serialize
#from .filters import MovieFilter, BookFilter, ShowFilter

# Create your views here.

class mydict(dict):
    def __str__(self):
        return json.dumps(self)

def is_valid_queryparam(param):
    print(param)
    return param != "" and param



def index(request):
    #data needed for index template: index.html
    #3 buttons for url to movies, books and tv shows
    return render(request, "index.html")


def movies(request):
    
    movies_query = Movie.objects.all()

    title_query = request.GET.get("title_contains") # query param
    year_query = request.GET.get("year_contains") 
    genre_query = request.GET.get("genre_contains") 
    director_query = request.GET.get("director_contains") 
    stars_query = request.GET.get("stars_contains") 
    rating_query = request.GET.get("rating_contains")
    oscar_query  = request.GET.get("oscar_contains")
    duration_query = request.GET.get("duration_contains")


    if is_valid_queryparam(title_query):
        movies_query = movies_query.filter(title__icontains=title_query)
    if is_valid_queryparam(year_query):
        movies_query = movies_query.filter(year__icontains=year_query)
    if is_valid_queryparam(genre_query):
        movies_query = movies_query.filter(genre__icontains=genre_query)
    if is_valid_queryparam(director_query):
        movies_query = movies_query.filter(director__icontains=director_query)
    if is_valid_queryparam(stars_query):
        movies_query = movies_query.filter(stars__icontains=stars_query)
    if is_valid_queryparam(rating_query):
        movies_query = movies_query.filter(rating__gte=rating_query)
    if is_valid_queryparam(oscar_query):
        movies_query = movies_query.filter(oscar__icontains=oscar_query)
    if duration_query != "" and duration_query:
        movies_query = movies_query.filter(duration__icontains=duration_query)

    

    movies_list = movies_query.values_list("id", flat=True)
    random.shuffle(list(movies_list))


    movies_random = random.sample(list(movies_list), min(len(movies_list), 10))
    movies_query = movies_query.filter(id__in=movies_random)

    movies = list(list([] for _ in range(2)) for _ in range(len(movies_query)))
    #print(movies)
    print(len(movies))
    
    for i in range(len(list(movies_query.values()))):
        movies[i][0] = "label", list(movies_query.values())[i]["title"]
        movies[i][1] = "value", 1
        movies[i] = mydict(movies[i])
    movies = json.dumps(movies)
    print(movies)
    

    return render(request, "movies.html", {"movies":movies})
    

def books(request):
    books = Book.objects.all()

    title_query = request.GET.get("title_contains")
    author_query = request.GET.get("author_contains")
    rating_query = request.GET.get("rating_contains")


    if is_valid_queryparam(title_query):
        books = books.filter(title__icontains=title_query)
    if is_valid_queryparam(author_query):
        books = books.filter(author__icontains=author_query)
    if is_valid_queryparam(rating_query):
        books = books.filter(rating__gte=rating_query)

    books = random.sample(books, min(books.objects.count(), 10))


    return render(request, "books.html", {"books": books})



def shows(request):
    shows = TVShow.objects.all()

    title_query = request.GET.get("title_contains")
    year_query = request.GET.get("year_contains")
    genre_query = request.GET.get("genre_contains") 
    stars_query = request.GET.get("stars_contains")
    rating_query = request.GET.get("rating_contains")
    duration_query = request.GET.get("duration_contains")


    if is_valid_queryparam(title_query):
        movies = movies.filter(title__icontains=title_query)
    if is_valid_queryparam(year_query):
        movies = movies.filter(year__icontains=year_query)
    if is_valid_queryparam(genre_query):
        movies = movies.filter(genre__icontains=genre_query)
    if is_valid_queryparam(stars_query):
        movies = movies.filter(stars__icontains=stars_query)
    if is_valid_queryparam(rating_query):
        movies = movies.filter(rating__gte=rating_query)


    shows = random.sample(shows, min(shows.objects.count(), 10))




    return render(request, "shows.html", {"shows": shows})
