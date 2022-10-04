from django.db import models


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