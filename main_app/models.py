from django.db import models

# Create your models here.


class Chip(models.Model):
    flavor = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    rating = models.IntegerField()

    def __str__(self):
        return f'{self.flavor} ({self.id})'