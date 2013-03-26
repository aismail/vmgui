from nose.tools import eq_, ok_, raises
from django.forms import ValidationError
from django.contrib.auth.models import User

from vmc_backend.forms.submission_form import SubmissionForm
from vmc_backend.tests.base_model_form_test_case import BaseModelFormTestCase
from vmc_backend.factories import (SubmissionFactory, AssignmentFactory,
                        UserFactory, SubjectFactory)
from vmc_backend.models import Assignment


class TestSubmissionForm(BaseModelFormTestCase):
    def test_assignment_exists(self):
        ass = AssignmentFactory()
        subm = SubmissionFactory(assignment=ass)
        ass.delete()
        self.assertRaises(Assignment.DoesNotExist, SubmissionForm, subm)

    def test_student_exists(self):
        stud = UserFactory()
        subm = SubmissionFactory(student=stud)
        stud.delete()
        self.assertRaises(User.DoesNotExist, SubmissionForm, subm)

    def test_student_is_enrolled_at_the_subject(self):
        stud1 = UserFactory()
        subj1 = SubjectFactory()
        ass = AssignmentFactory(subject=subj1)
        subm = SubmissionFactory(student=stud1, assignment=ass)
        self.assertRaises(ValidationError,SubmissionForm,subm)
