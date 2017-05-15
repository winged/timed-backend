# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-12 11:17
from __future__ import unicode_literals

from django.db import migrations, models
import timed.models


class Migration(migrations.Migration):

    dependencies = [
        ('employment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='workdays',
            field=timed.models.WeekdaysField(choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (7, 'Sunday')], default=['1', '2', '3', '4', '5'], max_length=13),
        ),
        migrations.AlterField(
            model_name='location',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
