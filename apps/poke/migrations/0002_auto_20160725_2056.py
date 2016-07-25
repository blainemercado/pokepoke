# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-25 20:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('poke', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('userManager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='lvl',
            field=models.PositiveSmallIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='user',
            name='p1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='poke.Pokemon'),
        ),
        migrations.AlterField(
            model_name='user',
            name='p2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Pokemon2', to='poke.Pokemon'),
        ),
        migrations.AlterField(
            model_name='user',
            name='p3',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Pokemon3', to='poke.Pokemon'),
        ),
    ]
