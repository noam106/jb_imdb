from django.db import models

# Create your models here.


class Movie(models.Model):

    name = models.CharField(null=False, blank=False, max_length=128)
    description = models.TextField(null=True, blank=True)
    duration_in_min = models.IntegerField(null=False, blank=True)
    release_year = models.IntegerField(null=True, blank=True)
