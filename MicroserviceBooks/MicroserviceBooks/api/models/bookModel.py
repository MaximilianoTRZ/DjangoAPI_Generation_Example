from django.db import models
from .authorModel import Author
from .genreModel import Genre

class Book(models.Model):
    title = models.CharField(max_length=100) 
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    summary = models.CharField(max_length=100) 
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        ordering = ['title']

    def __str__(self):
        return self.title