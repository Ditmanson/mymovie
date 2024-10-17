# app/models.py
from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    # Add other fields as necessary

    def __str__(self):
        return self.title
