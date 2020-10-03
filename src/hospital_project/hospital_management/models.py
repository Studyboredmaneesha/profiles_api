from django.db import models

# Create your models here.


class Doctor(models.Model):
    name = models.CharField(max_length=50)
    department = models.CharField(max_length=100)
    telephone = models.IntegerField()

    def __str__(self):
        return self.name

class Patient(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    age = models.IntegerField()
    telephone = models.IntegerField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
