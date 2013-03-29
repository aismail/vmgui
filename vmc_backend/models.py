from django.db import models
from vmc_backend.core.base_model import BaseModel
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator


class Subject(BaseModel):
    """ Subject Model, referring to a course, for example.

    Fields: name, description, link
    Methods: contact_emails

    Example name: 'Sisteme de Operare'
            link: 'http://ocw.cs.pub.ro/courses/so'
    """
    name = models.CharField(max_length=30,
            help_text='Full name of the subject, such as "Sisteme de Operare"',
            unique=True,
            validators=[MinLengthValidator(3)])
    description = models.TextField(blank=True,
            help_text='Descriptive information regarding the subject; \
                    this field is optional')
    link = models.URLField(max_length=200,
            blank=True,
            help_text='An URL to additional information about the subject')

    class Meta:
        ordering = ['name']

    def contact_email_list(self):
        """ Return a list of contact emails for Subject, based on the
            available_for_contact field in UsersToSubjects
        """
        u2s = self.userstosubjects_set.filter(available_for_contact=True)
        return [ s.user.email for s in u2s ]

    def __str__(self):
        return self.name


class Assignment(BaseModel):
    subject = models.ForeignKey(Subject)
    name = models.CharField(max_length=30)
    text = models.TextField()
    deadline = models.DateTimeField()
    attachments = models.URLField(blank=True)

    def __str__(self):
        return self.name


class UsersToSubjects(BaseModel):
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
    available_for_contact = models.BooleanField(default=False)

    def __str__(self):
        return str(self.subject.pk) + "-" + str(self.user.pk)


class Submission(BaseModel):
    student = models.ForeignKey(User, related_name='submissions')
    assignment = models.ForeignKey(Assignment, related_name='assignments')
    # This is a timestamp
    uploaded_at = models.DateTimeField(auto_now_add=True)
    graded = models.BooleanField(default=False)
    content = models.FileField(upload_to='uploads')

    def __str__(self):
        return str(self.student.pk) + "-" + str(self.assignment.pk) + \
            "-" + str(self.uploaded_at)


class SubmissionComment(BaseModel):
    submission = models.ForeignKey(Submission, related_name='comments')
    filename = models.CharField(max_length=256, blank=True)
    line_no = models.IntegerField(null=True, blank=True)
    comment = models.TextField()

    def __str__(self):
        return str(self.submission.pk) + "-" + str(self.comment)
