from django.db import models

# Create your models here.

class Reminder(models.Model):
    text = models.TextField(blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)
    reminder = models.DateTimeField()
    active = models.BooleanField(default=True)