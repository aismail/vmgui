from vmc_backend.core.base_model_form import BaseModelForm
from vmc_backend.models import Submission, Assignment


class SubmissionForm(BaseModelForm):
    class Meta:
        model = Submission
    def clean(self):
        cleaned_data = super(SubmissionForm, self).clean()

        from nose.tools import set_trace; set_trace()
        ass = cleaned_data.get('assignment')

        Assignment.objects.get(pk=ass.pk)

        return cleaned_data
