from tastypie.test import ResourceTestCase
from vmc_backend.api.resources import SubjectResource
from vmc_backend.factories import SubjectFactory

class SubjectResourceTest(ResourceTestCase):
    def setUp(self):
        super(SubjectResourceTest, self).setUp()
        
        self.subject_1 = SubjectFactory()
        self.subject_2 = SubjectFactory()

        self.detail_url = '/api/v1/subject/{0}/'.format(self.subject_1.pk)

    def test_get_detail_json(self):
        resp = self.api_client.get(self.detail_url, format='json')
        self.assertValidJSONResponse(resp)

    def test_get_list_json(self):
        resp = self.api_client.get('/api/v1/subject/', format='json')
        self.assertValidJSONResponse(resp)

        self.assertEqual(len(self.deserialize(resp)['objects']), 2)
