from tastypie.test import ResourceTestCase

from vmc_backend.factories import UsersToSubjectsFactory, SubjectFactory, UserFactory

class UsersToSubjectsResourceTest(ResourceTestCase):

    def setUp(self):
        super(UsersToSubjectsResourceTest, self).setUp()
        self.u2s1 = UsersToSubjectsFactory()
        self.u2s2 = UsersToSubjectsFactory()
        self.base_url = '/api/v1/userstosubjects/'

    def test_get_valid_json_response_and_objects(self):
        resp = self.api_client.get(self.base_url, format='json')
        self.assertValidJSONResponse(resp)
        deserialized_resp = self.deserialize(resp)
        self.assertEqual(len(deserialized_resp['objects']), 2)
        self.assertEqual(deserialized_resp['objects'][1]['id'], self.u2s2.pk)

    def test_filter_by_user(self):
        resp = self.api_client.get(self.base_url + '?user_id=%s' %self.u2s1.user_id, format = 'json')
        deserialized_resp = self.deserialize(resp)
        self.assertEqual(len(deserialized_resp['objects']), 1)
        self.assertEqual(deserialized_resp['objects'][0]['id'], self.u2s1.pk)

        #Tests if a user with no userstosubjects returns an empty list.
        user_with_no_users_to_subjects_mapping = UserFactory()
        resp = self.api_client.get(self.base_url + '?user_id=%s' %user_with_no_users_to_subjects_mapping.pk, format = 'json')
        self.assertEqual(len(self.deserialize(resp)['objects']), 0)
