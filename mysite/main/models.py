from django.db import models
#from custom.fields import SeparatedValuesField
# Create your models here.



class Movie(models.Model):
    """
    fields: title, year, genre, 
            Director, Stars, IMDb, 
            Oscar, Duration

    """
    movie_title = models.CharField(max_length=255)
    movie_year = models.IntegerField()
    movie_genre = models.TextField()
    movie_director = models.CharField(max_length=255)
    movie_stars = models.TextField()
    movie_rating = models.FloatField()
    movie_oscar = models.CharField(max_length=10)
    movie_duration = models.IntegerField()


    def __str__(self):
        return self.movie_title



class Book(models.Model):
    """
    fields: title, author, rating, img_src

    """
    book_title = models.CharField(max_length=255)
    book_author = models.CharField(max_length=255)
    book_rating = models.FloatField()
    book_img_src = models.TextField()

    def __str__(self):
        return self.book_title



class TVShow(models.Model):
    """
    fields: title, year, genre, Stars, rating, duration
    """

    show_title = models.CharField(max_length=255)
    show_year = models.IntegerField()
    show_genre = models.TextField()
    show_stars = models.TextField()
    show_rating = models.FloatField()


    def __str__(self):
        return self.show_title



    

