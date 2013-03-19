import datetime
from tastypie.test import ResourceTestCase
from vmc_backend.api.resources import SubmissionResource
from vmc_backend.factories import SubmissionFactory
from vmc_backend.models import Submission
from django.contrib.auth.models import User


class SubjectResourceTest(ResourceTestCase):
    def setUp(self):
        super(SubjectResourceTest, self).setUp()
        
        self.subm1 = SubmissionFactory()
        self.subm2 = SubmissionFactory()
        # Create a user.
        self.username = 'user'
        self.password = 'pass'
        self.user = User.objects.create_user(self.username,
                        'daniel@example.com', self.password)

        self.detail_url = '/api/v1/submission/{0}/'.format(self.subm1.pk)
        self.post_data = {
            'user': '/api/v1/user/{0}/'.format(self.user.pk),  
            'assignment_id': '<Assignment: fd27e50eb88455704dc0aa1eb4d9b5>',
            'student_id': '<User: 4bc17e76edea0760902dd155fefae3>',
            'uploaded_at': datetime.datetime(2013, 3, 18, 20, 1, 35, 399386),
            'graded': False,
        }
         
    def get_credentials(self):
        return self.create_basic(username=self.username, password=self.password)

    def test_get_detail_unauthenticated(self):
        self.assertHttpUnauthorized(self.api_client.get(self.detail_url, 
                                    format='json'))
    def test_get_detail_json(self):
        resp = self.api_client.get(self.detail_url, format='json', 
                                   authentication=self.get_credentials())
        self.assertValidJSONResponse(resp)

    def test_get_list_json(self):
        resp = self.api_client.get('/api/v1/submission/', format='json',
                                   authentication=self.get_credentials())
        self.assertValidJSONResponse(resp)
        self.assertEqual(len(self.deserialize(resp)['objects']), 2)

    def test_post_list_unauthenticated(self):
        self.assertHttpUnauthorized(self.api_client.post('/api/v1/submission/',
                                    format='json', data=self.post_data)) 

    def test_post_list(self):
        # Check how many are there first.
        self.assertEqual(Submission.objects.count(), 2)
        # from nose.tools import set_trace; set_trace()
        self.assertHttpCreated(self.api_client.post('/api/v1/submission/',
                             format='json', data=self.post_data,
                             authentication=self.get_credentials()))
        # Verify a new one has been added.
        self.assertEqual(Submission.objects.count(), 3)

