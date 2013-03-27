from django.contrib.auth.models import User
from django.forms.models import model_to_dict

from vmc_backend.forms.submission_form import SubmissionForm
from vmc_backend.tests.base_model_form_test_case import BaseModelFormTestCase
from vmc_backend.factories import (SubmissionFactory, AssignmentFactory,
                        UserFactory, SubjectFactory, UsersToSubjectsFactory)


class TestSubmissionForm(BaseModelFormTestCase):
    def setUp(self):
        super(TestSubmissionForm, self).setUp()

        self.student = UserFactory()
        self.subject = SubjectFactory()
        self.assignment = AssignmentFactory()

    def test_assignment_exists(self):
        assignment1 = AssignmentFactory()
        submission = SubmissionFactory(assignment=assignment1)
        assignment1.delete()
        form = SubmissionForm(data=model_to_dict(submission))
        self.assertFalse(form.is_valid())
        self.assertTrue(('assignment') in form.errors.keys())

    def test_student_exists(self):
        student1 = UserFactory()
        submission = SubmissionFactory(student=student1)
        student1.delete()
        form = SubmissionForm(data=model_to_dict(submission))
        self.assertFalse(form.is_valid())
        self.assertTrue(('student') in form.errors.keys())

    def test_student_is_enrolled_at_the_subject(self):
        subject2 = SubjectFactory()
        UsersToSubjectsFactory(user=self.student, subject=subject2)
        assignment = AssignmentFactory(subject=self.subject)
        submission = SubmissionFactory(student=self.student,
                                       assignment=assignment)
        form = SubmissionForm(data=model_to_dict(submission))
        self.assertFalse(form.is_valid())
        self.assertTrue(('__all__') in form.errors.keys())
