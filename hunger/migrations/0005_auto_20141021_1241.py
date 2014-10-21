# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hunger', '0004_auto_20141016_1450'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodRating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating', models.IntegerField(default=0)),
                ('food', models.ForeignKey(to='hunger.Food')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Share',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('foodName', models.ForeignKey(to='hunger.Food')),
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
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='rating',
            name='food',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='user',
        ),
        migrations.DeleteModel(
            name='Rating',
        ),
        migrations.AddField(
            model_name='share',
            name='socialName',
            field=models.ForeignKey(to='hunger.SocialNetworking'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='foodrating',
            name='user',
            field=models.ForeignKey(to='hunger.User'),
            preserve_default=True,
        ),
        migrations.RemoveField(
            model_name='type',
            name='name',
        ),
        migrations.AddField(
            model_name='food',
            name='averageRating',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='type',
            name='type',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='food',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='phoneNumber',
            field=models.CharField(max_length=11),
        ),
    ]
