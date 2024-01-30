import csv
from django.core.management.base import BaseCommand
from movie_app.models import Movie, Genre

class Command(BaseCommand):
    help = 'Import movies from CSV file'

    def handle(self, *args, **options):
        Movie.objects.all().delete()  # Clear existing data

        with open('movie_app/movies.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                genres = [genre.strip() for genre in row['genres'].split(',')]
                movie = Movie.objects.create(title=row['title'])
                for genre in genres:
                    genre_obj, created = Genre.objects.get_or_create(name=genre)
                    movie.genres.add(genre_obj)