# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hunger', '0005_auto_20141021_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='type',
            field=models.ForeignKey(to='hunger.Type', null=True),
        ),
    ]
