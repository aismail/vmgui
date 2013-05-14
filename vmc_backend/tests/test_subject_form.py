from django.forms.models import model_to_dict

from vmc_backend.forms.subject_form import SubjectForm
from vmc_backend.tests.base_model_form_test_case import BaseModelFormTestCase
from vmc_backend.factories import (SubjectFactory)


class TestSubjectForm(BaseModelFormTestCase):

    def test_working_for_correct_data(self):
        subject = SubjectFactory.build()
        form = SubjectForm(model_to_dict(subject))
        self.assertTrue(form.is_valid()) 
