from django.forms.models import model_to_dict
from django.core.files.uploadedfile import SimpleUploadedFile

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
        assignment1 = AssignmentFactory()
        submission = SubmissionFactory(assignment=assignment1)
        assignment1.delete()
        data=model_to_dict(submission)
        file_data={ 'content': SimpleUploadedFile(submission.content.name,
                                                  submission.content.read())}
        form = SubmissionForm(data,file_data)
        self.assertFalse(form.is_valid())
        self.assertTrue(('assignment') in form.errors.keys())

    def test_student_exists(self):
        student1 = UserFactory()
        submission = SubmissionFactory(student=student1)
        student1.delete()
        data=model_to_dict(submission)
        file_data={ 'content': SimpleUploadedFile(submission.content.name,
                                                  submission.content.read())}
        form = SubmissionForm(data,file_data)
        self.assertFalse(form.is_valid())
        self.assertTrue(('student') in form.errors.keys())

    def test_student_is_enrolled_at_the_subject(self):
        subject2 = SubjectFactory()
        UsersToSubjectsFactory(user=self.student, subject=subject2)
        assignment = AssignmentFactory(subject=self.subject)
        submission = SubmissionFactory(student=self.student,
                                       assignment=assignment)
        data=model_to_dict(submission)
        file_data={ 'content': SimpleUploadedFile(submission.content.name,
                                                  submission.content.read())}
        form = SubmissionForm(data,file_data)
        self.assertFalse(form.is_valid())
        self.assertTrue(('__all__') in form.errors.keys())

    def test_working_for_correct_data(self):
        UsersToSubjectsFactory(user=self.student, subject=self.subject)
        assignment = AssignmentFactory(subject=self.subject)
        submission = SubmissionFactory(student=self.student,
                                       assignment=assignment)
        data=model_to_dict(submission)
        file_data={ 'content': SimpleUploadedFile(submission.content.name,
                                                  submission.content.read())}
        form = SubmissionForm(data,file_data)
        self.assertTrue(form.is_valid())
