""" This file contains tastypie resources for all models in vmc_backend """
from tastypie import fields
from tastypie.resources import ModelResource
from vmc_backend.models import Assignment, Subject, Submission
from tastypie.authentication import Authentication
from tastypie.authorization import Authorization

class SubmissionResource(ModelResource):
    student = fields.IntegerField(attribute='sudent_id')
    #assignment = fields.IntegerField(attribute= 'assignment_id')
    class Meta:
        queryset = Submission.objects.all()
        allowed_methods = ['get', 'post']
        authentication = Authentication()
        authorization = Authorization()
    def hydrate(self, bundle):
        #bundle.data['student_id']=self.request.POST['student']
        if not bundle.obj.pk:
            bundle.obj.student_id=self.student
        return bundle
    def dehydrate(self, bundle):
        #from nose.tools import set_trace; set_trace()
        bundle.data['student_id']=self.student
        return bundle


class AssignmentResource(ModelResource):
    class Meta:
        queryset = Assignment.objects.all()
        allowed_methods = ['get']


class SubjectResource(ModelResource):
    class Meta:
        queryset = Subject.objects.all()
        allowed_methods = ['get']
