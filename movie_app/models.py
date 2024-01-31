from django.db import models


# Create your models here.
class UserData(models.Model):
    username = models.CharField(max_length=80)
    email = models.EmailField(max_length=80)
    password = models.CharField(max_length=80)


class Genre(models.Model):
    name = models.CharField(max_length=255)


class Movie(models.Model):
    title = models.CharField(max_length=255)
    genres = models.ManyToManyField(Genre)
    poster_url = models.URLField()  # Assuming the poster is stored as a URL
    synopsis = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)


