from django.db import models
from django.utils.translation import gettext_lazy as _


class Author(models.Model):
    name = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100) 
    birthDay = models.DateField(auto_now=False, auto_now_add=False)

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
        ordering = ['name']
    
    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'
        ordering = ['name']
    
    def __str__(self):
        return self.name

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

class BookInstance(models.Model):
    class Status(models.TextChoices):
        Available = "Available", _("Available")
        Maintenance = "Maintenance", _("Maintenance")
        Loaned = "Loaned", _("Loaned")
        Reserved = "Reserved", _("Reserved")
    
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=15,
        choices=Status.choices,
        default=Status.Maintenance
    )
    return_date = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'BookInstance'
        verbose_name_plural = 'BookInstances'
        ordering = ['status']
    
    def __str__(self):
        return self.status
