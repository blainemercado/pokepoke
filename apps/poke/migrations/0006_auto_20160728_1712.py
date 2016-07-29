# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-28 17:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poke', '0005_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='p1',
            field=models.ForeignKey(default='empty', null=True, on_delete=django.db.models.deletion.CASCADE, to='poke.Pokemon'),
        ),
        migrations.AlterField(
            model_name='user',
            name='p2',
            field=models.ForeignKey(default='empty', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Pokemon2', to='poke.Pokemon'),
        ),
        migrations.AlterField(
            model_name='user',
            name='p3',
            field=models.ForeignKey(default='empty', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Pokemon3', to='poke.Pokemon'),
        ),
    ]