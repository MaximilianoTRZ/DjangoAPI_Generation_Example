from django.db import models

# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)


    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'
        ordering = ['name']
    
    def __str__(self):
        return self.name

# Extends from Person, since person is abstract
# it only implements the child (Client).
class Client(models.Model):
    name = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    birthDay = models.DateField(auto_now=False, auto_now_add=False)
    
    # Relation with hasRoutes: False
    class personAddress(models.Model):
        street = models.CharField(max_length=100)
        number = models.IntegerField()
        # Relation to attribute with hasRoutes: true
        addressCity = models.ForeignKey(City, on_delete=models.CASCADE, blank=True, null=True,)
        # Relation to class outside of microservice
        rentedBooks = models.IntegerField() 

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
        ordering = ['name']
    
    def __str__(self):
        return self.name

