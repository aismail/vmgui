""" This file contains tastypie resources for all models in vmc_backend """
from tastypie import fields
from tastypie.resources import ALL
from vmc_backend.core.base_resource import BaseResource
from vmc_backend.models import Assignment, Subject, Submission, UsersToSubjects
from tastypie.authentication import Authentication
from tastypie.authorization import Authorization


class SubmissionResource(BaseResource):
    student_id = fields.IntegerField(attribute='student_id')
    assignment_id = fields.IntegerField(attribute='assignment_id')

    class Meta(BaseResource.Meta):
        filtering = {
            'assignment_id': ALL,
        }
        queryset = Submission.objects.all()
        allowed_methods = ['get', 'post']
        authentication = Authentication()
        authorization = Authorization()


class AssignmentResource(BaseResource):
    subject_id = fields.IntegerField(attribute='subject_id')

    class Meta(BaseResource.Meta):
        filtering = {
            "subject_id": ALL,
            "id": ALL,
        }
        queryset = Assignment.objects.all()
        allowed_methods = ['get', 'post']


class SubjectResource(BaseResource):

    class Meta(BaseResource.Meta):
        queryset = Subject.objects.all()
        allowed_methods = ['get']
        resource_name = 'subjects'

    def dehydrate(self, bundle):
        bundle.data['contact_emails'] = bundle.obj.contact_email_list()
        return bundle


class UsersToSubjectsResource(BaseResource):
    subject_id = fields.IntegerField(attribute='subject_id')
    user_id = fields.IntegerField(attribute='user_id')

    class Meta(BaseResource.Meta):
        filtering = {
            "user_id": ALL,
        }
        queryset = UsersToSubjects.objects.all()
        allowed_methods = ['get']
