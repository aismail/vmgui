from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    link = models.URLField(max_length=200)
    