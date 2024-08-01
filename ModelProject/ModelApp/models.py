from django.db import models

# Create your models here.
class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    mobile = models.BigIntegerField()
    dob = models.DateField()
    gen = [
        ("male","Male"),
        ("female","Female"),
        ("others","Others")
    ]
    gender = models.CharField(max_length=10,choices=gen,default="others")

    def __str__(self):
         return f'{self.name} {self.email}'

class Staff(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    mobile = models.BigIntegerField()
    city = models.CharField(max_length=20, default= "")
    dob = models.DateField()

    def __str__(self):
        return f'{self.name} {self.email}'