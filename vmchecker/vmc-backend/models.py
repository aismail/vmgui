from django.db import models
from django.contrib.auth.models import User

class Subject(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    link = models.URLField(max_length=200)
    

class Assignment(models.Model):
    subject_id = models.ForeignKey(Subject)
    text = models.TextField()
    deadline = models.DateField()
    attachments = models.URLField()

class UsersToSubjects(models.Model):
    unique_together = ("subject_id", "user_id")
    subject_id = models.ForeignKey(Subject)
    user_id = models.ForeignKey(User)
    role_choices = (
            ('teacher', 'Teacher'),
            ('student', 'Student'),
            )
    role = models.CharField(max_length = 15,
                            choices = role_choices,
                            default = 'student')

class Submission(models.Model):
    student_id = models.ForeignKey(User, related_name='submissions')
    assignment_id = models.ForeignKey(Assignment, related_name='assignments')
    uploaded_at = models.DateTimeField()
    graded = models.BooleanField()
    comment_count = models.IntegerField()
    content = BinaryField()

class SubmissionComment(models.Model):
    submission_id = models.ForeignKey(Submission)
    filename = models.CharField(max_length=256)
    line_no = models.IntegerField()
    comment_no = models.IntegerField()
    comment = models.TextField()


