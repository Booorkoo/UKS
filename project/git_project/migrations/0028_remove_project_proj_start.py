# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-26 14:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('git_project', '0027_auto_20170226_1457'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='proj_start',
        ),
    ]
