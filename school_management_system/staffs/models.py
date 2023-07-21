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


class std_messages(models.Model):
    """ For Teachers sending message to a Particular CLASS  """
    message_id =models.AutoField(primary_key=True)
    date = models.DateField(auto_now=False, auto_now_add=True)  #auto_now= updates every time , auto_now_add = updates only when instance is created
    std_standard = models.CharField(max_length=50)
    head = models.CharField(max_length=100)
    content = models.CharField(max_length=350)

    """ ADD: teacher_name and student to submit assignment """


