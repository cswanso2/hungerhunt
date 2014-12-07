# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('hunger', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='type',
            name='restaurant',
        ),
        migrations.DeleteModel(
            name='Type',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='facebookId',
            field=models.CharField(max_length=120, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='foodrating',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 7, 20, 54, 46, 603433), auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='socialstat',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 7, 20, 54, 46, 604179), auto_now=True),
            preserve_default=True,
        ),
    ]
