from vmc_backend.core.base_model_form import BaseModelForm
from vmc_backend.models import Assignment


class AssignmentForm(BaseModelForm):
    class Meta:
        model = Assignment

