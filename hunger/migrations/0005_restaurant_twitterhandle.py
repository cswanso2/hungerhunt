# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hunger', '0004_auto_20141202_1835'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='twitterHandle',
            field=models.CharField(default='mcdonalds', max_length=50),
            preserve_default=False,
        ),
    ]
