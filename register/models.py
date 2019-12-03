from django.db import models

# Create your models here.
class Register(models.Model):

    username = models.CharField(max_length=150)
    email = models.CharField(max_length=100)
    phone = models.IntegerField()
    date_of_birth = models.DateField()