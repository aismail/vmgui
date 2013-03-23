from nose.tools import eq_, ok_

from forms import SubjectForm
from tests.base_model_form_test_case import BaseModelFormTestCase

class TestSubjectForm(BaseModelFormTestCase):
    
    def test_form_can_be_instantiated(self):
        """ Assert a form instance can be created
        """
        form = SubjectForm()
        eq_(form.data, {})