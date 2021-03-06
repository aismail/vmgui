from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator

from vmc_backend.core.base_model import BaseModel


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
    """ Assignment refers to a homework set by a teacher for a subject.
    """
    subject = models.ForeignKey(Subject,
            help_text='The subject this assignment is set for')
    name = models.CharField(max_length=30,
            help_text='Full name of the assignment',
            unique=True,
            validators=[MinLengthValidator(3)])
    text = models.TextField(help_text='Description of the assignment')
    deadline = models.DateTimeField(help_text='The date and hour until \
            submissions from students are accepted')
    attachments = models.URLField(max_length=200,
            blank=True,
            help_text='An URL to resources needed to solve the assignment. \
                    This field is optional.')
    class Meta:
        ordering = ['name']

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
    """ Submission model refers to a homework solution sent by a student.
    """

    student = models.ForeignKey(User, related_name='submissions',
            help_text="The user who sent the submission")
    assignment = models.ForeignKey(Assignment, related_name='assignments',
            help_text="The assignment this submission is sent for")
    # This is a timestamp
    uploaded_at = models.DateTimeField(auto_now_add=True,
            help_text="The time when the submission was sent")
    graded = models.BooleanField(default=False,
            help_text="Specifies if the teacher graded the submission")
    content = models.FileField(upload_to='uploads',
            help_text="The archive containing the files of the submission")

    class Meta:
        ordering = ['-uploaded_at']

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
