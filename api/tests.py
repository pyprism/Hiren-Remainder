from django.test import TestCase, TransactionTestCase
from django.shortcuts import reverse
from rest_framework.test import APIRequestFactory, APIClient
from freezegun import freeze_time
from django.contrib.auth.models import User
# Create your tests here.


class TestToken(TestCase):

    def setUp(self):
        self.client = APIClient()
        User.objects.create_user('hiren', 'a@b.com', 'password')

    def test_auth_token(self):
        response = self.client.post(reverse("token"), {'username': 'hiren', 'password': 'password'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue('token' in response.json())

    def test_error(self):
        response = self.client.post(reverse("token"), {'username': 'hiren', 'password': 'bad password'})
        self.assertEqual(response.status_code, 401)
        self.assertTrue('error' in response.json())


class ReminderViewTest(TransactionTestCase):
    reset_sequences = True

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user('hiren', 'a@b.com', 'password')
        self.client.force_authenticate(user=self.user)

    def test_login_works(self):
        response = self.client.get('/api/reminder/reminder/')
        self.assertEqual(response.status_code, 200)

        self.client.logout()
        response = self.client.get('/api/reminder/reminder/')
        self.assertEqual(response.status_code, 403)
