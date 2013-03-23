from tastypie.test import ResourceTestCase

from vmc_backend.factories import UsersToSubjectsFactory, SubjectFactory, UserFactory

class UsersToSubjectsResourceTest(ResourceTestCase):

    def setUp(self):
        super(UsersToSubjectsResourceTest, self).setUp()
        self.u2s1 = UsersToSubjectsFactory()
        self.u2s2 = UsersToSubjectsFactory()
        self.subjectwithnousers = SubjectFactory(pk=123)

    def test_get_valid_json_response(self):
        resp = self.api_client.get('/api/v1/userstosubjects/', format='json')
        self.assertValidJSONResponse(resp)

    def test_get_all_objects_and_in_order(self):
        resp = self.api_client.get('/api/v1/userstosubjects/', format='json')
        self.assertEqual(len(self.deserialize(resp)['objects']), 2)
        self.assertEqual(self.deserialize(resp)['objects'][1]['id'], self.u2s2.id)

    def test_filter_by_user(self):
        resp = self.api_client.get('/api/v1/userstosubjects/?user_id=%s' %self.u2s1.user_id, format = 'json')
        self.assertEqual(len(self.deserialize(resp)['objects']), 1)
        self.assertEqual(self.deserialize(resp)['objects'][0]['id'], self.u2s1.id)

        """Tests if a subject with no users returns an empty list.
        """
        resp = self.api_client.get('/api/v1/userstosubjects/?user_id=%s' %self.subjectwithnousers.pk, format = 'json')
        self.assertEqual(len(self.deserialize(resp)['objects']), 0)
