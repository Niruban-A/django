from django.db import models

# Create your models here.
class Article(models.Model):
    name=models.TextField()
    price=models.IntegerField()
