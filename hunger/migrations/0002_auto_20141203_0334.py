# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hunger', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='totalLikes',
            new_name='totalLike',
        ),
        migrations.RenameField(
            model_name='restaurant',
            old_name='totalTweets',
            new_name='totalTweet',
        ),
    ]
