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
    #3 buttons for url to shows, books and tv shows
    return render(request, "index.html")


def books(request):
    
    books_query = Book.objects.all()
    #print(len(books_query))

    title_query = request.GET.get("title_contains") # query param
    author_query = request.GET.get("author_contains") 
    rating_query = request.GET.get("rating_gte")
    genre_query = request.GET.get("genre_contains")
    

    if is_valid_queryparam(title_query):
        books_query = books_query.filter(title__icontains=title_query)
    if is_valid_queryparam(author_query):
        books_query = books_query.filter(author__icontains=author_query)
    if is_valid_queryparam(rating_query):
        books_query = books_query.filter(rating__gte=rating_query)
    if is_valid_queryparam(genre_query):
        books_query = books_query.filter(genre__icontains=genre_query)

    

    books_list = books_query.values_list("id", flat=True)
    random.shuffle(list(books_list))


    books_random = random.sample(list(books_list), min(len(books_list), 54))
    books_query = books_query.filter(id__in=books_random)

    books = list(list([] for _ in range(2)) for _ in range(len(books_query)))
    book_details = list(list() for _ in range(len(books_query)))
    raw_details_books = list(list() for _ in range(len(books_query)))

    #print(books)
    print(len(books))
    
    for i in range(len(list(books_query.values()))):
        books[i][0] = "label", list(books_query.values())[i]["title"]
        books[i][1] = "value", 1
        books[i] = mydict(books[i])
    books = json.dumps(books)
    #print(books)

    for i in range(len(list(books_query.values()))):
        book_details[i] = list(books_query.values())[i]
        book_details[i] = mydict(book_details[i])
    
    #print(book_details)


    for i in range(len(list(books_query.values()))):
        l = {"id":0, "genre":[],"img_src":0, "title":0,"rating":3, "author":7}
        element = list(books_query.values())[i]
        l["id"] = (element["id"])
        l["genre"] = (element["genre"])
        l["img_src"] =(element["img_src"])
        l["title"] =(element["title"])
        l["rating"] =(element["rating"])
        l["element"] =(element["author"])

        raw_details_books[i] = l

    raw_details_books = json.dumps(raw_details_books)


    print("raw_details_books:",raw_details_books)

    return render(request, "books.html", {"books":books, "book_details":book_details, "raw_details_books":raw_details_books})

def shows(request):
    
    shows_query = TVShow.objects.all()

    title_query = request.GET.get("title_contains") # query param
    year_query = request.GET.get("year_contains") 
    genre_query = request.GET.get("genre_contains") 
    #director_query = request.GET.get("director_contains") 
    stars_query = request.GET.get("stars_contains") 
    rating_query = request.GET.get("rating_contains")
    #oscar_query  = request.GET.get("oscar_contains")
    duration_query = request.GET.get("duration_contains")


    if is_valid_queryparam(title_query):
        shows_query = shows_query.filter(title__icontains=title_query)
    if is_valid_queryparam(year_query):
        shows_query = shows_query.filter(year__gte=year_query)
    if is_valid_queryparam(genre_query):
        shows_query = shows_query.filter(genre__icontains=genre_query)
    if is_valid_queryparam(stars_query):
        shows_query = shows_query.filter(stars__icontains=stars_query)
    if is_valid_queryparam(rating_query):
        shows_query = shows_query.filter(rating__gte=rating_query)
    if duration_query != "" and duration_query:
        shows_query = shows_query.filter(duration__icontains=duration_query)

    

    shows_list = shows_query.values_list("id", flat=True)
    random.shuffle(list(shows_list))


    shows_random = random.sample(list(shows_list), min(len(shows_list), 54))
    shows_query = shows_query.filter(id__in=shows_random)

    shows = list(list([] for _ in range(2)) for _ in range(len(shows_query)))
    shows_details = list(list() for _ in range(len(shows_query)))
    raw_details_shows = list(list() for _ in range(len(shows_query)))

    print(len(shows))
    
    for i in range(len(list(shows_query.values()))):
        shows[i][0] = "label", list(shows_query.values())[i]["title"]
        shows[i][1] = "value", 1
        shows[i] = mydict(shows[i])
    shows = json.dumps(shows)

    
    for i in range(len(list(shows_query.values()))):
        l = {"id":0, "genre":[], "stars":[], "img_src":0, "title":0, "year":0, "rating":3, "duration":0, "YT_link":3}
        element = list(shows_query.values())[i]
        element["img_src"] = element["img_src"][1:-1]
        l["id"] = (element["id"])
        l["genre"] = (element["genre"])
        l["stars"] =(element["stars"])
        l["img_src"] =(element["img_src"])
        l["title"] =(element["title"])
        l["year"] =(element["year"])
        l["rating"] =(element["rating"])
        l["duration"] =(element["duration"])
        l["YT_link"] = element["YT_link"]

        raw_details_shows[i] = l
        #movies_details[i] = mydict(movies_details[i])
    



    for i in range(len(list(shows_query.values()))):
        l = [["id",0], ["genre",[]], ["stars",[]], ["img_src",0], ["title",0], ["year",0], ["rating",3], ["duration", 0], ["YT_link", 3]]
        element = list(shows_query.values())[i]
        element["img_src"] = element["img_src"][1:-1]
        l[0][1] = (element["id"])
        l[1][1] = (element["genre"])
        l[2][1] =(element["stars"])
        l[3][1] =(element["img_src"])
        l[4][1] =(element["title"])
        l[5][1] =(element["year"])
        l[6][1] =(element["rating"])
        l[7][1] =(element["duration"])
        l[8][1] = element["YT_link"]

        shows_details[i] = l
        shows_details[i] = mydict(shows_details[i])

    shows_details = json.dumps(shows_details)  
    print(shows_details)

    return render(request, "shows.html", {"shows":shows, "shows_details":shows_details, "raw_details_shows":raw_details_shows})

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
        movies_query = movies_query.filter(year__gte=year_query)
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
    if is_valid_queryparam(duration_query):
        movies_query = movies_query.filter(duration__icontains=duration_query)

    

    movies_list = movies_query.values_list("id", flat=True)
    random.shuffle(list(movies_list))


    movies_random = random.sample(list(movies_list), min(len(movies_list), 56))
    movies_query = movies_query.filter(id__in=movies_random)

    movies = list(list([] for _ in range(2)) for _ in range(len(movies_query)))
    movies_details = list(list() for _ in range(len(movies_query)))
    raw_details = list(list() for _ in range(len(movies_query)))

    #print(movies)
    print(len(movies))
    
    for i in range(len(list(movies_query.values()))):
        movies[i][0] = "label", list(movies_query.values())[i]["title"]
        movies[i][1] = "value", 1
        movies[i] = mydict(movies[i])
    movies = json.dumps(movies)
    #print(movies)
    
    for i in range(len(list(movies_query.values()))):
        l = {"id":0, "genre":[], "stars":[], "director":[], "img_src":0, "title":0, "year":0, "rating":3, "oscar":False, "duration":0, "YT_link":3}
        element = list(movies_query.values())[i]
        element["img_src"] = element["img_src"][1:-1]
        l["id"] = (element["id"])
        l["genre"] = (element["genre"])
        l["stars"] =(element["stars"])
        l["director"] =(element["director"])
        l["img_src"] =(element["img_src"])
        l["title"] =(element["title"])
        l["year"] =(element["year"])
        l["rating"] =(element["rating"])
        l["oscar"] =(element["oscar"])
        l["duration"] =(element["duration"])
        l["YT_link"] = element["YT_link"]

        raw_details[i] = l
        #movies_details[i] = mydict(movies_details[i])
    



    for i in range(len(list(movies_query.values()))):
        l = [["id",0], ["genre",[]], ["stars",[]], ["director",[]], ["img_src",0], ["title",0], ["year",0], ["rating",3], ["oscar",False], ["duration", 0], ["YT_link", 3]]
        element = list(movies_query.values())[i]
        element["img_src"] = element["img_src"][1:-1]
        l[0][1] = (element["id"])
        l[1][1] = (element["genre"])
        l[2][1] =(element["director"])
        l[3][1] =(element["stars"])
        l[4][1] =(element["img_src"])
        l[5][1] =(element["title"])
        l[6][1] =(element["year"])
        l[7][1] =(element["rating"])
        l[8][1] =(element["duration"])
        l[9][1] =(element["oscar"])
        l[10][1] = element["YT_link"]

        movies_details[i] = l
        movies_details[i] = mydict(movies_details[i])

    movies_details = json.dumps(movies_details)  
    print(movies_details)  

    return render(request, "movies.html", {"movies":movies, "movies_details":movies_details, "raw_details":raw_details})








