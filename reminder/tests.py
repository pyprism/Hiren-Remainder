from django.urls import resolve
from django.test import TestCase, TransactionTestCase
from django.contrib.auth.models import User
from django.test import Client
from . import views
from .models import Profile, Reminder
from freezegun import freeze_time
from django.utils import timezone


class ModelTest(TransactionTestCase):
    reset_sequences = True

    @freeze_time("2012-01-14")
    def setUp(self):
        self.user = User.objects.create_user('hiren', 'a@b.com', 'bunny')
        Reminder.objects.create(user=self.user, date_time=timezone.now(), title="hello", text="hiren", email=True)

    def test_reminder_model(self):
        count = Reminder.objects.count()
        self.assertEqual(count, 1)

        reminder = Reminder.objects.get(pk=1)
        self.assertEqual(reminder.title, "hello")
