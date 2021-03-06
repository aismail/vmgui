from django.forms import ValidationError

from vmc_backend.core.base_model_form import BaseModelForm
from vmc_backend.models import Submission, UsersToSubjects


class SubmissionForm(BaseModelForm):
    class Meta:
        model = Submission
        exclude = ('uploaded_at', )

    def clean_subject_and_assignment(self):
        """ Checks if the student is enrolled on the subject of the assignment 
        he tries to sent a submission for.
        Raises ValidationError if he is not.
        """
        if ('student' in self.cleaned_data.keys() and \
            'assignment' in self.cleaned_data.keys()): 
            student = self.cleaned_data['student']
            assignment = self.cleaned_data['assignment']
            subject = assignment.subject
            u2s = UsersToSubjects.objects.all().filter(user=student,
                    subject=subject)
            if not u2s:
                raise ValidationError('Student not enrolled at this subject')

    def clean(self):
        cleaned_data = super(SubmissionForm, self).clean()
        self.clean_subject_and_assignment()

        return cleaned_data
