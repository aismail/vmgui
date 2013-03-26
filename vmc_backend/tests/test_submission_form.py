from nose.tools import eq_, ok_, raises

from vmc_backend.forms.submission_form import SubmissionForm
from vmc_backend.tests.base_model_form_test_case import BaseModelFormTestCase
from vmc_backend.factories import SubmissionFactory, AssignmentFactory
from vmc_backend.models import Assignment


class TestSubmissionForm(BaseModelFormTestCase):
    def test_assignment_exists(self):

        ass = AssignmentFactory()
        subm = SubmissionFactory(assignment=ass)
        ass.delete()
        self.assertRaises(Assignment.DoesNotExist,form = SubmissionForm(subm))

