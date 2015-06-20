from django.db import models

# Create your models here.

class Reminder(models.Model):
    text = models.TextField(blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)
    reminder_date = models.DateField(null=False, blank=False)
    reminder_time = models.TimeField(null=False, blank=False)
    active = models.BooleanField(default=True)