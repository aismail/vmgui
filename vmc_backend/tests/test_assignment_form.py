from django.forms.models import model_to_dict

from vmc_backend.forms.assignment_form import AssignmentForm
from vmc_backend.tests.base_model_form_test_case import BaseModelFormTestCase
from vmc_backend.factories import (AssignmentFactory, SubjectFactory)


class TestAssignmentForm(BaseModelFormTestCase):
    def test_subject_exists(self):
        subject = SubjectFactory()
        assignment = AssignmentFactory.build(subject=subject)
        subject.delete()
        form = AssignmentForm(model_to_dict(assignment))
        self.assertFalse(form.is_valid())
        self.assertTrue(('subject') in form.errors.keys())

    def test_working_for_correct_data(self):
        subject = SubjectFactory()
        assignment = AssignmentFactory.build(subject=subject)
        form = AssignmentForm(model_to_dict(assignment))
        form.full_clean()
        self.assertTrue(form.is_valid())
