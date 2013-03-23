from django.db import models
from django.contrib.auth.models import User


class Subject(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    link = models.URLField(max_length=200, blank=True)
    contact_person_email = models.EmailField(blank=True)

    def __str__(self):
        return self.name


class Assignment(models.Model):
    subject = models.ForeignKey(Subject)
    name = models.CharField(max_length=30)
    text = models.TextField()
    deadline = models.DateTimeField()
    attachments = models.URLField(blank=True)

    def __str__(self):
        return self.name


class UsersToSubjects(models.Model):
    unique_together = ("subject_id", "user_id")
    subject = models.ForeignKey(Subject)
    user = models.ForeignKey(User)
    role_choices = (
            ('teacher', 'Teacher'),
            ('assistant', 'Assistant'),
            ('student', 'Student'),
            )
    role = models.CharField(max_length=15,
                            choices=role_choices,
                            default='student')

    def __str__(self):
        return str(self.subject.pk) + "-" + str(self.user.pk)


class Submission(models.Model):
    student = models.ForeignKey(User, related_name='submissions')
    assignment = models.ForeignKey(Assignment, related_name='assignments')
    # This is a timestamp
    uploaded_at = models.DateTimeField(auto_now_add=True)
    graded = models.BooleanField(default=False)
    content = models.FileField(upload_to='uploads')

    def __str__(self):
        return str(self.student.pk) + "-" + str(self.assignment.pk) + \
            "-" + str(self.uploaded_at)


class SubmissionComment(models.Model):
    submission = models.ForeignKey(Submission, related_name='comments')
    filename = models.CharField(max_length=256, blank=True)
    line_no = models.IntegerField(null=True, blank=True)
    comment = models.TextField()

    def __str__(self):
        return str(self.submission.pk) + "-" + str(self.comment)
