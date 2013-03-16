""" This file contains tastypie resources for all models in vmc_backend """

from tastypie.resources import ModelResource
from vmc_backend.models import Subject


class SubjectResource(ModelResource):
    class Meta:
        queryset = Subject.objects.all()
        allowed_methods = ['get']
