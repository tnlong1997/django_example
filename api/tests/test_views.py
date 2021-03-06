from rest_framework.test import APITestCase
from ..models import User
from django.shortcuts import reverse


class UserListViewTest(APITestCase):
    def setUp(self):
        self.user_list_url = reverse('user-list')
        self.data = {
            'username': 'test',
            'password': 'test',
        }

    def test_user_list_post(self):
        response = self.client.post(self.user_list_url, self.data)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(response.status_code, 201)

    # def test_user_list_get(self):
    #     response = self.client.get(self.user_list_url, format='json')
    #     self.assertEqual(len(response.data), 1)
