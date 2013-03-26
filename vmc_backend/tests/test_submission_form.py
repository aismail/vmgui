from nose.tools import eq_, ok_

from vmc_backend.forms.submission_form import SubmissionForm
from vmc_backend.tests.base_model_form_test_case import BaseModelFormTestCase


class TestSubmissionForm(BaseModelFormTestCase):

    def test_form_can_be_instantiated(self):

        form = SubmissionForm()
        eq_(form.data, {})
