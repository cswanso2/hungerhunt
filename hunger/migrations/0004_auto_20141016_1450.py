# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hunger', '0003_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='picture',
            field=models.CharField(default='notset', max_length=120),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='location',
            field=models.CharField(max_length=100),
        ),
    ]
