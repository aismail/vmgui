from tastypie.resources import ModelResource
from tastypie.serializers import Serializer

class BaseResource(ModelResource):
    class Meta:
        serializer = Serializer(formats=['json'])
