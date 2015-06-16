__author__ = 'prism'
# date : 10-6-2015

from .models import Reminder
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')


class ReminderSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(read_only=True)
    active = serializers.BooleanField(default=True)
    reminder = serializers.DateTimeField()

    class Meta:
        model = Reminder
        fields = ('text', 'created', 'reminder', 'active')
