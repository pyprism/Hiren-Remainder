from rest_framework import serializers
from reminder.models import Reminder


class ReminderSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Reminder
        fields = "__all__"

