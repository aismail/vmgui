"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
import datetime
from django.utils.timezone import utc
from django.conf import settings
from django.test import TestCase
from django.contrib.auth.models import User
import logging
from models import Subject, Assignment, UsersToSubjects, Submission,\
    SubmissionComment

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

class AssignmentModelTest(TestCase):

    #checks if the attachments field is set as optional
    def test_optional_field(self):
        testsubject = Subject(name = "testname", description = "testdescription", link = "http://www.google.ro/")
        testsubject.save()
        now = datetime.datetime.utcnow().replace(tzinfo=utc)
        testassignment = Assignment(subject_id = testsubject, name="test", text = "asda", deadline = now)
        testassignment.save()
        testsubject.delete()
        testassignment.delete()

