from django.db import models
from django.contrib.auth.models import User

class Subject(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    link = models.URLField(max_length=200)
    contact_person_email = models.EmailField()

class Assignment(models.Model):
    subject_id = models.ForeignKey(Subject)
    text = models.TextField()
    deadline = models.DateField()
    attachments = models.URLField()

class UsersToSubjects(models.Model):
    subject_id = models.ForeignKey(Subject)
    user_id = models.ForeignKey(User)
    role = models.CharField(max_length = 15)
    unique_together = ("subject_id", "user_id")

