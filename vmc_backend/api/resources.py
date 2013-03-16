""" This file contains tastypie resources for all models in vmc_backend """
from tastypie.resources import ModelResource
from vmc_backend.models import Submission

class SubmissionResource(ModelResource):
    class Meta:
        queryset = Submission.objects.all()
        allowed_methods = ['get']
