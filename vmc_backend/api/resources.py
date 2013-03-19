""" This file contains tastypie resources for all models in vmc_backend """
from tastypie.resources import ModelResource
from vmc_backend.models import Assignment, Subject, Submission
from tastypie.authentication import BasicAuthentication

class SubmissionResource(ModelResource):
    class Meta:
        queryset = Submission.objects.all()
        allowed_methods = ['get', 'post']
        authentication = BasicAuthentication()


class AssignmentResource(ModelResource):
    class Meta:
        queryset = Assignment.objects.all()
        allowed_methods = ['get']


class SubjectResource(ModelResource):
    class Meta:
        queryset = Subject.objects.all()
        allowed_methods = ['get']
