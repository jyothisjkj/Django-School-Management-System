from django.db import models

# Create your models here.


class Student(models.Model):
    roll_number = models.CharField(max_length=50,primary_key=True,unique=True)
    name = models.CharField(max_length=150)
    standard = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    email  = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password =models.CharField(max_length=150)
