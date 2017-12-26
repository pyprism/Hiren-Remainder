from django.test import TestCase, TransactionTestCase
from django.shortcuts import reverse
from rest_framework.test import APIRequestFactory, APIClient
from freezegun import freeze_time
from django.contrib.auth.models import User
from reminder.models import Reminder
from django.utils import timezone
import json


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

    @freeze_time("2012-05-12")
    def setUp(self):
        self.client = APIClient()
        self.date = timezone.now()
        self.user = User.objects.create_user('hiren', 'a@b.com', 'password')
        self.client.force_authenticate(user=self.user)
        Reminder.objects.create(user=self.user, date_time=self.date, title="text", text="bugs bunny!")

    def test_login_works(self):
        response = self.client.get('/api/reminder/')
        self.assertEqual(response.status_code, 200)

        self.client.logout()
        response = self.client.get('/api/reminder/')
        self.assertEqual(response.status_code, 403)

    def test_correct_reminder_returns(self):
        response = self.client.get("/api/reminder/1/")
        self.assertEqual(response.json(), {'id': 1, 'active': True, 'date_time': '2012-05-12T00:00:00', 'title': 'text',
                                           'text': 'bugs bunny!', 'email': False, 'sms': False, 'desktop': False,
                                           'mobile': False, 'created_at': '2012-05-12T00:00:00',
                                           'updated_at': '2012-05-12T00:00:00'})

    @freeze_time("2012-05-12")
    def test_reminder_update(self):
        response = self.client.patch("/api/reminder/1/", data={"title": "new title"})
        self.assertEqual(response.json(), {'id': 1, 'active': True, 'date_time': '2012-05-12T00:00:00', 'title': 'new title',
                                           'text': 'bugs bunny!', 'email': False, 'sms': False, 'desktop': False,
                                           'mobile': False, 'created_at': '2012-05-12T00:00:00',
                                           'updated_at': '2012-05-12T00:00:00'})

    # @freeze_time("2012-05-12")
    # def test_reminder_create(self):
    #     response = self.client.post("/api/reminder/", data=json.dumps({"date_time": "2012-05-12T00:00:00",
    #                                 "title": "text", "text": "bugs bunny!"}))
    #     print(response.json())








