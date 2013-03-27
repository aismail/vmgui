from django.contrib.auth.models import User
from django.forms.models import model_to_dict

from vmc_backend.forms.submission_form import SubmissionForm
from vmc_backend.tests.base_model_form_test_case import BaseModelFormTestCase
from vmc_backend.factories import (SubmissionFactory, AssignmentFactory,
                        UserFactory, SubjectFactory, UsersToSubjectsFactory)


class TestSubmissionForm(BaseModelFormTestCase):
    def setUp(self):
        super(TestSubmissionForm, self).setUp()

        self.student = UserFactory()
        self.subject = SubjectFactory()
        self.assignment = AssignmentFactory()

    def test_assignment_exists(self):
        assignment = AssignmentFactory()
        subm = SubmissionFactory(assignment=assignment)
        assignment.delete()
        form = SubmissionForm(data=model_to_dict(subm))
        self.assertTrue((('assignment') in form.errors.keys()) and
                (form.errors['assignment'].pop() ==
    'Select a valid choice. That choice is not one of the available choices.'))

    def test_student_exists(self):
        stud = UserFactory()
        subm = SubmissionFactory(student=stud)
        stud.delete()
        form = SubmissionForm(data=model_to_dict(subm))
        self.assertTrue((('student') in form.errors.keys()) and
                (form.errors['student'].pop() ==
    'Select a valid choice. That choice is not one of the available choices.'))

    def test_student_is_enrolled_at_the_subject(self):
        stud1 = UserFactory()
        subj1 = SubjectFactory()
        subj2 = SubjectFactory()
        UsersToSubjectsFactory(user=stud1, subject=subj2)
        assignment = AssignmentFactory(subject=subj1)
        subm = SubmissionFactory(student=stud1, assignment=assignment)
        form = SubmissionForm(data=model_to_dict(subm))
        self.assertTrue((('__all__') in form.errors.keys()) and
            form.errors['__all__'].pop() == 'Student not enrolled at this subject')
