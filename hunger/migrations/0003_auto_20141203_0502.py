# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('hunger', '0002_auto_20141203_0334'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='socialstat',
            name='numberOfTweets',
        ),
        migrations.AddField(
            model_name='foodrating',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 3, 5, 2, 58, 581796), auto_now=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='socialstat',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 3, 5, 2, 58, 582701), auto_now=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='socialstat',
            name='tweet',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
