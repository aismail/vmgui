from nose.tools import ok_, eq_
from tastypie.test import ResourceTestCase

from vmc_backend.factories import AssignmentFactory

class AssignmentResourceTest(ResourceTestCase):

    def setUp(self):
        super(AssignmentResourceTest, self).setUp()
        self.as1 = AssignmentFactory()
        self.as2 = AssignmentFactory()
        self.detail_url = '/api/v1/assignment/{0}/'.format(self.as1.pk)

    def test_get_detail_json(self):
        resp = self.api_client.get(self.detail_url, format = 'json')
        self.assertValidJSONResponse(resp)

    def test_get_list_json(self):
        resp = self.api_client.get('/api/v1/assignment/', format='json')
        self.assertValidJSONResponse(resp)
        self.assertEqual(len(self.deserialize(resp)['objects']), 2)
        self.assertEqual(self.deserialize(resp)['objects'][1]['id'], self.as2.id)
        
    def test_filter_by_subject(self):
        """ Assert assignments are filtered by a certain subject
        """
        # Create two assignments with separate subjects
        ok_(self.as1.subject_id, self.as2.subject_id)
        
        

