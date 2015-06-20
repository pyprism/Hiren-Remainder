# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('reminder', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reminder',
            name='reminder',
        ),
        migrations.AddField(
            model_name='reminder',
            name='reminder_date',
            field=models.DateField(default=datetime.datetime(2015, 6, 20, 4, 59, 49, 370933, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reminder',
            name='reminder_time',
            field=models.TimeField(default=datetime.datetime(2015, 6, 20, 5, 0, 18, 914329, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
