from django.db import models
from .cityModel import City

class Address(models.Model):
    street = models.CharField(max_length=100)
    number = models.IntegerField(default=0)
    city = models.CharField(max_length=100, unique=True)
    addressCity = models.OneToOneField(City, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'
        ordering = ['street']
    
    def __str__(self):
        return self.street