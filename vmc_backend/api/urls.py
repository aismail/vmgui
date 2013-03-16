from django.conf.urls.defaults import *
from tastypie.api import Api

v1_api = Api(api_name='v1')

urlpatterns = patterns('',
    (r'^', include(v1_api.urls))
)
