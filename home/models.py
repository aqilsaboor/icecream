from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=50)
    number = models.CharField(max_length=12)
    email = models.CharField(max_length=30)
    decr = models.CharField(max_length=300)
    date = models.DateField()
    def __str__(self):
        return self.name
    
# Create your models here.
