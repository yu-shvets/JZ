# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-27 09:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('JZ', '0003_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Name')),
                ('comment', models.TextField(verbose_name='Comment')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JZ.Project')),
            ],
            options={
                'verbose_name': 'Feedback',
                'verbose_name_plural': 'Feedback',
            },
        ),
    ]
