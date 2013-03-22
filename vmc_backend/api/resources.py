""" This file contains tastypie resources for all models in vmc_backend """
from tastypie import fields
from tastypie.resources import ModelResource
from vmc_backend.models import Assignment, Subject, Submission, UsersToSubjects
from tastypie.authentication import Authentication
from tastypie.authorization import Authorization

class SubmissionResource(ModelResource):
    student_id = fields.IntegerField(attribute='student_id')
    assignment_id = fields.IntegerField(attribute='assignment_id')

    class Meta:
        queryset = Submission.objects.all()
        allowed_methods = ['get', 'post']
        authentication = Authentication()
        authorization = Authorization()


class AssignmentResource(ModelResource):
    class Meta:
        queryset = Assignment.objects.all()
        allowed_methods = ['get']


class SubjectResource(ModelResource):
    class Meta:
        queryset = Subject.objects.all()
        allowed_methods = ['get']

class UsersToSubjectsResource(ModelResource):
    class Meta:
        queryset = UsersToSubjects.objects.all()
        allowed_methods = ['get']
