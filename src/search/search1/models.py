from django.db import models
from django.contrib.auth.models import Model
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Food(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=4)
    category = models.ForeignKey(category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# Create your models here.
