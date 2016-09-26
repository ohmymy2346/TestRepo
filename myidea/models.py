from django.db import models

# Create your models here.
class Article(models.Model):
    username=models.CharField(max_length=200)
    topic=models.CharField(max_length=200)
    description=models.CharField(max_length=900)
