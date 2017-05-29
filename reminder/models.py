from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    twillo_sid = models.CharField(max_length=100, blank=True, null=True)
    twillo_token = models.CharField(max_length=100, blank=True, null=True)
    twillo_from_no = models.CharField(max_length=100, blank=True, null=True)
    twillo_to_no = models.CharField(max_length=100, blank=True, null=True)
    mailgun_api_url = models.URLField(blank=True, null=True)
    mailgun_api_key = models.CharField(max_length=100, null=True, blank=True)
    mailgun_from = models.CharField(max_length=100, null=True, blank=True)
    mailgun_to = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Reminder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    date_time = models.DateTimeField()
    title = models.CharField(max_length=200)
    text = models.TextField()
    email = models.BooleanField(default=False)
    sms = models.BooleanField(default=False)
    desktop = models.BooleanField(default=False)
    mobile = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
