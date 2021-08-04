from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

# TODO: Create an Employee model with properties required by the user stories
class Employees(models.Model):
    name = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=5)
    user = models.ForeignKey('account.User', blank=True, null=True, on_delete=models.CASCADE)
