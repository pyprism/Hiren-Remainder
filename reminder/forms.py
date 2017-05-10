from django.forms import ModelForm
from .models import Profile, Reminder


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)


class ReminderForm(ModelForm):
    class Meta:
        model = Reminder
        exclude = ('user', )
