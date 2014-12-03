# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('price', models.CharField(max_length=10)),
                ('averageRating', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FoodRating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating', models.IntegerField(default=0)),
                ('food', models.ForeignKey(to='hunger.Food')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Nutrition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fat', models.IntegerField()),
                ('protein', models.IntegerField()),
                ('sugar', models.IntegerField()),
                ('carbs', models.IntegerField()),
                ('calories', models.IntegerField()),
                ('food', models.OneToOneField(to='hunger.Food')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=100)),
                ('faceBookLikeURL', models.URLField(default=False)),
                ('hasTwitter', models.BooleanField()),
                ('twitterHandle', models.CharField(max_length=50)),
                ('phoneNumber', models.CharField(max_length=11)),
                ('picture', models.CharField(max_length=120)),
                ('totalTweets', models.IntegerField(default=0)),
                ('totalLikes', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SocialNetworking',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SocialStat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numberOfTweets', models.IntegerField(default=0)),
                ('likedOnOurSite', models.BooleanField(default=False)),
                ('restaurant', models.ForeignKey(to='hunger.Restaurant')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('typeR', models.CharField(max_length=20)),
                ('restaurant', models.ForeignKey(to='hunger.Restaurant', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='food',
            name='restaurant',
            field=models.ForeignKey(to='hunger.Restaurant'),
            preserve_default=True,
        ),
    ]
