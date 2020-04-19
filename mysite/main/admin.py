from django.contrib import admin
from .models import Movie, Book, TVShow
# Register your models here.


admin.site.register(Movie)
admin.site.register(Book)
admin.site.register(TVShow)