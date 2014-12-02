# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hunger', '0003_restaurant_hastwitter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='faceBookLikeURL',
            field=models.URLField(default=False),
            preserve_default=True,
        ),
    ]
