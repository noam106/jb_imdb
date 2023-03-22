from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.


class Movie(models.Model):

    name = models.CharField(null=False, blank=False, max_length=128)
    description = models.TextField(null=True, blank=True)
    duration_in_min = models.IntegerField(null=True, blank=True)
    release_year = models.IntegerField(null=True, blank=True)


    def __str__(self):
        return f'Id{self.id}, name: {self.name}'

    class Meta:
        db_table = 'movies'


class Review(models.Model):
    rating = models.FloatField(null=False, blank=False, validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])
    review_date = models.DateField(null=True, blank=True)
    review_text = models.TextField(null=True, blank=True)
    movie = models.ForeignKey('Movie', models.RESTRICT, null=True, blank=True)

    class Meta:
        db_table = 'reviews'

    def __str__(self):
        return f'movie name: {self.movie.name}, rating: {self.rating}'
