from django.db import models

class Users(models.Model):
    name     = models.CharField(max_length=30)
    password = models.CharField(max_length=50)

    class Meta:
        db_table = 'users'
# Create your models here.
