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


class LoginViewTest(TestCase):
    """
    Test for authentication
    """

    def setUp(self):
        User.objects.create_user('hiren', 'a@b.com', 'password')
        self.c = Client()

    def test_login_url_resolves_to_login_view(self):
        found = resolve('/')
        self.assertEqual(found.func, views.index)

    def test_auth(self):
        respond = self.c.post('/', {'username': 'hiren', 'password': 'password'})
        self.assertRedirects(respond, '/reminders/')

    def test_redirect_for_unauthenticated_user_works(self):
        response = self.c.get('/reminders/')
        self.assertRedirects(response, '/?next=/reminders/')

    def test_redirect_works_for_bad_auth(self):
        respond = self.c.post('/', {'username': 'hiren', 'password': 'bad pass'})
        self.assertRedirects(respond, '/')

    def test_view_returns_correct_template(self):
        response = self.c.get('/')
        self.assertTemplateUsed(response, 'login.html')

    def test_authenticated_user_redirect_to_the_app(self):
        self.c.login(username='hiren', password='password')
        response = self.c.get('/', follow=True)
        self.assertRedirects(response, '/reminders/')


class LogoutViewTest(TestCase):
    """
    Test logout
    """

    def setUp(self):
        User.objects.create_user('hiren', 'a@b.com', 'password')
        self.c = Client()

    def test_redirect_works(self):
        self.c.post('/', {'username': 'hiren', 'password': 'password'})
        respond = self.c.get('/logout/')
        self.assertRedirects(respond, '/')


class CreateViewTest(TransactionTestCase):
    """
    Test for create view
    """
    reset_sequences = True

    def setUp(self):
        self.c = Client()
        self.user = User.objects.create_user('hiren', 'a@b.com', 'bunny')

    def test_login_create_resolves_to_create_view(self):
        found = resolve('/create/')
        self.assertEqual(found.func, views.create)

    def test_view_returns_correct_template(self):
        self.c.login(username='hiren', password='bunny')
        response = self.c.get('/create/')
        self.assertTemplateUsed(response, 'add.html')

    @freeze_time("2012-01-14")
    def test_form(self):
        self.c.login(username='hiren', password='bunny')
        response = self.c.post('/create/', {
            'date_time': timezone.datetime.now(), 'title': 'hello',
            'text': 'meow', 'email': True
        }, follow=True)
        message = list(response.context.get('messages'))[0]
        self.assertEqual(message.message, 'New Reminder Added')

        self.assertRedirects(response, '/create/')

        reminder = Reminder.objects.count()
        self.assertEqual(reminder, 1)

    def test_redirect_for_unauthenticated_user_works(self):
        response = self.c.get('/create/')
        self.assertRedirects(response, '/?next=/create/')


class ProfileViewTest(TransactionTestCase):
    """
    Test for profile view
    """
    reset_sequences = True

    def setUp(self):
        self.c = Client()
        self.user = User.objects.create_user('hiren', 'a@b.com', 'bunny')

    def test_login_create_resolves_to_create_view(self):
        found = resolve('/profile/')
        self.assertEqual(found.func, views.profile)

    def test_view_returns_correct_template(self):
        self.c.login(username='hiren', password='bunny')
        response = self.c.get('/profile/')
        self.assertTemplateUsed(response, 'profile.html')

    @freeze_time("2012-01-14")
    def test_form(self):
        self.c.login(username='hiren', password='bunny')
        response = self.c.post('/profile/', {
            'twillo_sid': "blah blah"
        }, follow=True)
        message = list(response.context.get('messages'))[0]
        self.assertEqual(message.message, 'Profile Information Updated')

        self.assertRedirects(response, '/profile/')

    def test_redirect_for_unauthenticated_user_works(self):
        response = self.c.get('/profile/')
        self.assertRedirects(response, '/?next=/profile/')