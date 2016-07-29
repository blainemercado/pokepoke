# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-28 23:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poke', '0006_user_win'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='lose',
            field=models.PositiveSmallIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='user',
            name='win',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]
