from tastypie.test import ResourceTestCase
from vmc_backend.api.resources import SubmissionResource
from vmc_backend.factories import SubmissionFactory

class SubjectResourceTest(ResourceTestCase):
    def setUp(self):
        super(SubjectResourceTest, self).setUp()
        
        self.subm1 = SubmissionFactory()
        self.subm2 = SubmissionFactory()

        self.detail_url = '/api/v1/submission/{0}/'.format(self.subm1.pk)

    def test_get_detail_json(self):
        resp = self.api_client.get(self.detail_url, format='json')
        self.assertValidJSONResponse(resp)

    def test_get_list_json(self):
        resp = self.api_client.get('/api/v1/submission/', format='json')
        self.assertValidJSONResponse(resp)

        self.assertEqual(len(self.deserialize(resp)['objects']), 2)
