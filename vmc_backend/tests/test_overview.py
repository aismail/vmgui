"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.

TODO: This file has to be split UP for every file. test_submission.py
"""
import datetime

from django.utils.timezone import utc
from django.test import TestCase

from vmc_backend.models import Assignment, Subject, Submission
from vmc_backend.factories import (AssignmentFactory, SubjectFactory,
                                   SubmissionFactory, SubmissionCommentFactory,
                                   UsersToSubjectsFactory)


# the class below is just for learning purposes. It's going to be deleted.
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

    # checks if the attachments field is set as optional
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

