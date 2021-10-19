from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    image = models.ImageField()
    decription = models.TextField(max_length=None)
    stock = models.IntegerField()
    
    def __str__(self):
        return self.title

        