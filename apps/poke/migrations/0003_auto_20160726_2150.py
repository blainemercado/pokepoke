# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-26 21:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('poke', '0002_auto_20160725_2056'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='pokemon',
            managers=[
                ('pokemonManager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='pokemon',
            name='pokeid',
            field=models.PositiveSmallIntegerField(null=True),
        ),
    ]
