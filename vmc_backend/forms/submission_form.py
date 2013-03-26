from vmc_backend.core.base_model_form import BaseModelForm
from vmc_backend.models import Submission


class SubmissionForm(BaseModelForm):
    class Meta:
        model = Submission
