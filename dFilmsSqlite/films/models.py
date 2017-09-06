from __future__ import unicode_literals
from django.db import models
from django.urls import reverse


class Acteur(models.Model):
    acteur_name = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('films:acteurdetail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.acteur_name


class Film(models.Model):
    acteurs = models.ForeignKey(Acteur)
    film_title = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('films:filmdetail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.film_title
