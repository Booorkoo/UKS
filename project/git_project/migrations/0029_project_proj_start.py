# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-26 14:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('git_project', '0028_remove_project_proj_start'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='proj_start',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
