import django_filters
from .models import Movie, Book, TVShow
"""

class MovieFilter(django_filters.FilterSet):

    class Meta:
        model = Movie
        fields = ('title, ')



class ShowFilter(django_filters.FilterSet):

    class Meta:
        model = TVShow
        fields = ()



class BookFilter(django_filters.FilterSet):

    class Meta:
        model = Book
        fields = ()


"""