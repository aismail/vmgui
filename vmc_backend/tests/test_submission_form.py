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
        assignment = AssignmentFactory()
        subm = SubmissionFactory(assignment=assignment)
        data = {'student': subm.student.pk,
                'assignment': subm.assignment.pk,
                'uploaded_at': subm.uploaded_at,
                'graded': subm.graded,
                'content': subm.content,
                }
        assignment.delete()
        form = SubmissionForm(data)
        form.is_valid()
        self.assertTrue(form._errors.has_key('assignment') and
                (form._errors['assignment'].pop() ==
    'Select a valid choice. That choice is not one of the available choices.'))

    def test_student_exists(self):
        stud = UserFactory()
        subm = SubmissionFactory(student=stud)
        stud.delete()
        self.assertRaises(User.DoesNotExist, SubmissionForm, subm)

    def test_student_is_enrolled_at_the_subject(self):
        stud1 = UserFactory()
        subj1 = SubjectFactory()
        assignment = AssignmentFactory(subject=subj1)
        subm = SubmissionFactory(student=stud1, assignment=assignment)
        self.assertRaises(ValidationError,SubmissionForm,subm)
