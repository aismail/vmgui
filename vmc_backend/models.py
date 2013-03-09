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
    subject_id = models.ForeignKey(Subject)
    name = models.CharField(max_length=30)
    text = models.TextField()
    deadline = models.DateTimeField()
    attachments = models.URLField(blank = True)

    def __str__(self):
        return self.name

class UsersToSubjects(models.Model):
    unique_together = ("subject_id", "user_id")
    subject_id = models.ForeignKey(Subject)
    user_id = models.ForeignKey(User)
    role_choices = (
            ('teacher', 'Teacher'),
            ('assistant', 'Assistant'),
            ('student', 'Student'),
            )
    role = models.CharField(max_length = 15,
                            choices = role_choices,
                            default = 'student')

    def __str__(self):
        return str(self.subject_id) + "-" + str(self.user_id)

class Submission(models.Model):
    student_id = models.ForeignKey(User, related_name='submissions')
    assignment_id = models.ForeignKey(Assignment, related_name='assignments')
    uploaded_at = models.DateTimeField()
    graded = models.BooleanField(default=False)
    comment_count = models.IntegerField()
<<<<<<< HEAD
    content = models.FileField(upload_to='files')

=======
    content = models.FileField(upload_to='vmc_backend/files')
    
>>>>>>> Changed required/optional fields in Subject and SubmissionComment Models.
    def __str__(self):
        return str(self.student_id) + "-" + str(self.assignment_id) + "-" + str(self.uploaded_at)

class SubmissionComment(models.Model):
    submission_id = models.ForeignKey(Submission)
    filename = models.CharField(max_length=256, blank=True)
    line_no = models.IntegerField(blank=True)
    comment_no = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return str(self.submission_id) + "-" + str(self.comment_no)
