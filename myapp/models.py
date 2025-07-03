from django.db import models
from myapp.models import *

# Create your models here.
class Patient(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email=models.EmailField()
    contact=models.CharField(max_length=20)
    medical_history=models.TextField()
    dateofbirth=models.DateField()

    def __str__(self):
        return self.firstname + "" + self.lastname

class Doctor(models.Model):
    fullname=models.CharField(max_length=100)
    doctorid=models.IntegerField(max_length=20)
    age=models.IntegerField()
    department=models.CharField(max_length=100)

    def __str__(self):
        return self.fullname

 #Ward Model - name, capacity, department, floor
class Ward(models.Model):
     name=models.CharField(max_length=100)
     capacity=models.IntegerField()
     department=models.CharField(max_length=100)
     floor=models.CharField(max_length=100)

     def __str__(self):
         return self.name

class Appointment(models.Model):
    name = models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=100)
    datetime=models.DateTimeField()
    department=models.CharField(max_length=100)
    doctor=models.CharField(max_length=100)
    message=models.TextField()

    def __str__(self):
        return self.name

class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    subject=models.CharField(max_length=100)
    message=models.TextField()

    def __str__(self):
        return self.name



