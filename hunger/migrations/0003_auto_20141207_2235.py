# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hunger', '0002_auto_20141207_2054'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacebookUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('access_token', models.CharField(max_length=1000)),
                ('facebook_id', models.BigIntegerField(default=0)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='foodrating',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 7, 22, 35, 26, 698705), auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='socialstat',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 7, 22, 35, 26, 699453), auto_now=True),
            preserve_default=True,
        ),
    ]
