"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from django.conf import settings
from django.test import TestCase
from django.contrib.auth.models import User
import logging
from models import Subject, Assignment, UsersToSubjects, Submission,\
    SubmissionComment

class TestSubmissionModel(TestCase):
    def test_graded(self):
        """
            Tests that submission.graded is false by default
        """
        sub = Submission()
        self.assertEqual(sub.graded, False)
