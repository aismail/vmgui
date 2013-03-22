"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
import datetime
import factory
from factories import *
from django.utils.timezone import utc
from django.conf import settings
from django.test import TestCase
from django.contrib.auth.models import User
import logging
from models import Subject, Assignment, UsersToSubjects, Submission,\
    SubmissionComment


#the class below is just for learning purposes. It's going to be deleted.
class LetsSeeIfTheFactoriesWorkProperlyTest(TestCase):
    def test_factories(self):
        subiect = SubjectFactory.create()
        subiect.delete()
        sc = AssignmentFactory.create()
        sc.delete()
        u2s = UsersToSubjectsFactory.create()
        u2s.delete()
        sm = SubmissionFactory.create()
        sm.delete()
        smc = SubmissionCommentFactory.create()
        smc.delete()


class TestSubmissionModel(TestCase):
    def test_graded(self):
        sub = Submission()
        self.assertEqual(sub.graded, False)


class AssignmentModelTest(TestCase):

    #checks if the attachments field is set as optional
    def test_optional_field(self):
        testsubject = Subject(name="testname", description="testdescription",
                              link="http://www.google.ro/")
        testsubject.save()
        now = datetime.datetime.utcnow().replace(tzinfo=utc)
        testassignment = Assignment(subject=testsubject, name="test",
                                    text="asda", deadline=now)
        testassignment.save()
        testsubject.delete()
        testassignment.delete()

class TestSubjectModel(TestCase):
    # checks if description, link, contact_person_email fields are optional
    def test_if_optional(self):
        subject = Subject(name='Test name for subject')
        subject.save()
        subject.delete()

