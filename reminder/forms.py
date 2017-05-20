from django.forms import ModelForm
from .models import Profile, Reminder, Provider


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)


class ProviderForm(ModelForm):
    class Meta:
        model = Provider
        fields = '__all__'


class ReminderForm(ModelForm):
    notification = ProfileForm

    class Meta:
        model = Reminder
        exclude = ('user', )
