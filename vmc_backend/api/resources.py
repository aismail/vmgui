""" This file contains tastypie resources for all models in vmc_backend """
from tastypie import fields
from tastypie.resources import ModelResource, ALL
from vmc_backend.models import Assignment, Subject, Submission, UsersToSubjects
from tastypie.authentication import Authentication
from tastypie.authorization import Authorization

class SubmissionResource(ModelResource):
    student_id = fields.IntegerField(attribute='student_id')
    assignment_id = fields.IntegerField(attribute='assignment_id')

    class Meta:
        filtering = {
            'assignment_id': ALL,
        }
        queryset = Submission.objects.all()
        allowed_methods = ['get', 'post']
        authentication = Authentication()
        authorization = Authorization()


class AssignmentResource(ModelResource):
    subject_id = fields.IntegerField(attribute='subject_id')

    class Meta:
        filtering = {
            "subject_id": ALL,
            "id": ALL,
        }
        queryset = Assignment.objects.all()
        allowed_methods = ['get', 'post']

    def determine_format(self, request):
        return 'application/json'

class SubjectResource(ModelResource):

    class Meta:
        queryset = Subject.objects.all()
        allowed_methods = ['get']

class UsersToSubjectsResource(ModelResource):
    subject_id = fields.IntegerField(attribute='subject_id')
    user_id = fields.IntegerField(attribute='user_id')

    class Meta:
        filtering = {
            "user_id": ALL,
        }
        queryset = UsersToSubjects.objects.all()
        allowed_methods = ['get']

    def determine_format(self, request):
        return 'application/json'
