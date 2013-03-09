from django.db import models
from django.contrib.auth.models import User

class Subject(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    link = models.URLField(max_length=200)
    contact_person_email = models.EmailField()

class Assignment(models.Model):
    subject_id = models.ForeignKey(Subject)
    text = models.CharField(max_length=2000)
    deadline = models.DateField()
    attachments = models.URLField()
