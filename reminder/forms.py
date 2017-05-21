from django.forms import ModelForm
from .models import Profile, Reminder


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)


class ReminderForm(ModelForm):
    notification = ProfileForm

    class Meta:
        model = Reminder
        exclude = ('user', )
