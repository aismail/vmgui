import datetime
from tastypie.test import ResourceTestCase
from vmc_backend.factories import SubmissionFactory
from vmc_backend.models import Submission
from django.contrib.auth.models import User


class SubmissionResourceTest(ResourceTestCase):
    def setUp(self):
        super(SubmissionResourceTest, self).setUp()

        self.subm1 = SubmissionFactory()
        self.subm2 = SubmissionFactory()
        # Create a user.
        self.username = 'daniel'
        self.password = 'pass'
        self.user = User.objects.create_user(self.username,
                        'daniel@example.com', self.password)

        self.detail_url = '/api/v1/submissions/%d/' % self.subm1.pk

        self.post_data = {
            'student_id': self.subm1.student_id,
            'assignment_id': self.subm1.assignment_id,
            'uploaded_at': datetime.datetime(2013, 3, 18, 20, 1, 35, 399386),
            'graded': False
        }

    def get_credentials(self):
        return self.create_basic(username=self.username, password=self.password)

    def test_get_detail_json(self):
        resp = self.api_client.get(self.detail_url, format='json',
                                   authentication=self.get_credentials())
        # from nose.tools import set_trace; set_trace()
        self.assertValidJSONResponse(resp)

    def test_get_list_json(self):
        resp = self.api_client.get('/api/v1/submissions/', format='json',
                                   authentication=self.get_credentials())
        self.assertValidJSONResponse(resp)
        self.assertEqual(len(self.deserialize(resp)['objects']), 2)

    def test_post_list(self):
        # Check how many are there first.
        self.assertEqual(Submission.objects.count(), 2)
        # from nose.tools import set_trace; set_trace()
        self.assertHttpCreated(self.api_client.post('/api/v1/submissions/',
                             format='json', data=self.post_data))
        # Verify a new one has been added.
        self.assertEqual(Submission.objects.count(), 3)

    def test_filtering_by_assignment(self):
        """ Asserts if filtering by assignment returns right objects
        """
        resp = self.api_client.get('/api/v1/submissions/?assignment_id={0}'.
               format(self.subm1.assignment_id), format='json')
        self.assertEqual(len(self.deserialize(resp)['objects']), 1)

        #Assert that the id of returned submission is the correct one
        self.assertEqual(self.deserialize(resp)['objects'][0]['id'],
                         self.subm1.pk)
