from tkinter import CASCADE
from django.db import models

class Comment(models.Model):
    comment    = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)
    user       = models.ForeignKey('users',on_delete=models.CASCADE)
    feed       = models.ForeignKey('feeds',on_delete=models.CASCADE)

    class Meta:
        db_table = 'comments'
# Create your models here.
