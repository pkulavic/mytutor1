# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-18 20:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tutorprofile', '0003_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='availability',
            name='time',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tutorprofile.Time'),
            preserve_default=False,
        ),
    ]
