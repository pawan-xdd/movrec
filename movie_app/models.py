from django.db import models


# Create your models here.
class UserData(models.Model):
    username = models.CharField(max_length=80)
    email = models.EmailField(max_length=80)
    password = models.CharField(max_length=80)

