# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-27 16:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JZ', '0005_feedback_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]