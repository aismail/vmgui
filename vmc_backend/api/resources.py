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

    def determine_format(self, request):
        return 'application/json'


class SubjectResource(BaseResource):

    class Meta(BaseResource.Meta):
        queryset = Subject.objects.all()
        allowed_methods = ['get']

    def dehydrate(self, bundle):
        contact_list = [ u.user.email for u in \
            bundle.obj.userstosubjects_set.filter(available_for_contact=True) ]
        bundle.data['contact_emails'] = contact_list
        return bundle

    def determine_format(self, request):
        return 'application/json'


class UsersToSubjectsResource(BaseResource):
    subject_id = fields.IntegerField(attribute='subject_id')
    user_id = fields.IntegerField(attribute='user_id')

    class Meta(BaseResource.Meta):
        filtering = {
            "user_id": ALL,
        }
        queryset = UsersToSubjects.objects.all()
        allowed_methods = ['get']

    def determine_format(self, request):
        return 'application/json'
