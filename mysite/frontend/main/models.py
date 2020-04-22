from django.db import models
#from custom.fields import SeparatedValuesField
# Create your models here.


class Movie(models.Model):
    """
    fields: title, year, genre, 
            #Director, Stars, IMDb, 
            #Oscar, Duration
    """
    title = models.CharField(max_length=255)
    year = models.IntegerField()
    genre = models.TextField()
    director = models.CharField(max_length=255)
    stars = models.TextField()
    rating = models.FloatField()
    oscar = models.CharField(max_length=10)
    duration = models.IntegerField()
    #id_field = models.IntegerField(primary_key=True)



    def __str__(self):
        return self.title



class Book(models.Model):
    """
    fields: title, author, rating, img_src

    """
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    rating = models.FloatField()
    img_src = models.TextField()
    #id_field = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.title



class TVShow(models.Model):
    """
    fields: title, year, genre, Stars, rating, duration
    """

    title = models.CharField(max_length=255)
    year = models.IntegerField()
    genre = models.TextField()
    stars = models.TextField()
    rating = models.FloatField()
    duration = models.IntegerField()
    #id_field = models.IntegerField(primary_key=True)



    def __str__(self):
        return self.title







    

