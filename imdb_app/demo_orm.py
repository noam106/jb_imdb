import os
import csv
import radar

os.environ["DJANGO_SETTINGS_MODULE"] = "imdb.settings"

import django
django.setup()

from imdb_app.models import *

if __name__ == '__main__':
    # Movie.objects.create(name='The matrix',description='The most blow mind movie of al time', duration_in_min=112, release_year=1999)
    # m = Movie(name='The dark knight',description='The best DC movie',duration_in_min= 152,release_year=2008).save()
    # Movie.objects.create(name= 'jhon wick',description = 'Very surprising movie',duration_in_min= 120,release_year=2014)
    # Movie.objects.get(id=2).delete()
    # movies = Movie.objects.all()
    # for movie in movies:
    #     print(movie.name)
    #
    # movies_2000 = Movie.objects.filter(release_year=2000)
    # print(movies_2000)
    #
    # # def upload_data(csv_raot: str):
    #
    # with open("C:\\Users\\USER001\\Downloads\\top250imdb.csv", 'r') as file:
    #     csvreader = csv.DictReader(file)
    #     for movie in csvreader:
    #         print(movie)
    #         new_m = None
    #         review_random_date = radar.random_datetime(start='2022-03-22', stop='2023-03-22')
    #         new_m = Movie(name=movie['Movie_Name'], release_year=movie['Release_date'])
    #         new_m.save()
    #         Review.objects.create(rating=movie['Rating'], review_date=review_random_date, movie_id=new_m.id)

    movies = Movie.objects.all()
    reviews = Review.object.all()
    movies_after_1990 = []
    for movie in movies:
        if movie.release_year > 1990:
            movies_after_1990.append(movie)
    print(movies_after_1990)

    movies_before_2000_sky = []
    for movie in movies:
        if movie.release_year < 2000 and 'sky' in movie.name:
            movies_before_2000_sky.append()
    print(movies_before_2000_sky)

    review_text = 'GREAT MOVIE'
    for review in reviews:
        if review.rating > 9.4:
            review.movie()


