from vmc_backend.core.base_model_form import BaseModelForm
from vmc_backend.models import Subject

class SubjectForm(BaseModelForm):

    class Meta:
        model = Subject
