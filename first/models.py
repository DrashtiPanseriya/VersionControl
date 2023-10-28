from django.db import models

class User(models.Model):
    username = models.CharField(max_length=15, unique=True, primary_key=True)
    first_name = models.CharField(max_length=20, blank=False)
    last_name = models.CharField(max_length=20)
    contact_number = models.CharField(max_length=10)
    password = models.CharField(max_length=128, default="")
    gender = models.CharField(max_length=1, choices= [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ])
    age = models.PositiveIntegerField()   

