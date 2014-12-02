# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hunger', '0002_auto_20141202_1808'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='hasTwitter',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
