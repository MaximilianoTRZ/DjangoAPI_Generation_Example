from django.db import models
from .addressModel import Address

class Client(models.Model):
    name = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    birthDay = models.DateField(auto_now=False, auto_now_add=False)
    personAddress = models.OneToOneField(Address, on_delete=models.CASCADE, blank=True, null=True)
    rentedBook = models.CharField(max_length=100, blank=True, null=True)
    subscriptionDate = models.DateField(auto_now=False, auto_now_add=False, unique=True)

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
        ordering = ['name']
    
    def __str__(self):
        return self.name