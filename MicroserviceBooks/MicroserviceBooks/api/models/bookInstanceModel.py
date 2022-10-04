from django.db import models
from django.utils.translation import gettext_lazy as _
from .bookModel import Book

class BookInstance(models.Model):
    class Status(models.TextChoices):
        Available = "Available", _("Available")
        Maintenance = "Maintenance", _("Maintenance")
        Loaned = "Loaned", _("Loaned")
        Reserved = "Reserved", _("Reserved")
        
    id = models.AutoField(primary_key=True)
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
        ordering = ['id']
    
    def __str__(self):
        return self.status