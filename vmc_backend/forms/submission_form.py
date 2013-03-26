from django.forms import ValidationError

from vmc_backend.core.base_model_form import BaseModelForm
from vmc_backend.models import Submission, Assignment


class SubmissionForm(BaseModelForm):
    class Meta:
        model = Submission

    def clean(self):
        cleaned_data = super(SubmissionForm, self).clean()
        assignment = cleaned_data.get('assignment')
        try:
            Assignment.objects.get(pk=assignment.pk)
        except(AttributeError):
            raise ValidationError('Select a valid choice.')

        return cleaned_data
