# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-28 23:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poke', '0005_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='win',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]