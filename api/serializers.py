from rest_framework import serializers
from reminder.models import Reminder


class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        exclude = ("user",)

