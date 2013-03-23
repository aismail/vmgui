# Create your views here.

import django.contrib.auth.decorators as auth_decorators
from django.conf import settings
import os, django

UPLOADED = settings.PROJECT_PATH+'/uploads'

def get_absolute_filename(filename='', safe=True):
    if not filename:
        return os.path.join(UPLOADED, 'index')
    if safe and '..' in filename.split(os.path.sep):
        return get_absolute_filename(filename='')
    return os.path.join(UPLOADED, filename)

@auth_decorators.login_required
def retrieve_file(request, filename=''):
    abs_filename = get_absolute_filename(filename)
    response = django.http.HttpResponse() # 200 OK
    del response['content-type'] # We'll let the web server guess this.
    response['X-Sendfile'] = abs_filename
    return response