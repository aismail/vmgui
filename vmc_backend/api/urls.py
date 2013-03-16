from django.conf.urls.defaults import *
from tastypie.api import Api
from vmc_backend.api.resources import AssignmentResource, SubjectResource

v1_api = Api(api_name='v1')
v1_api.register(SubjectResource())
v1_api.register(AssignmentResource())

urlpatterns = patterns('',
    (r'^', include(v1_api.urls))
)
