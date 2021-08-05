from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

# TODO: Create an Employee model with properties required by the user stories
class Employees(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey('accounts.User', blank=True, null=True, on_delete=models.CASCADE)
    zip_code = models.CharField(max_length=50)
    