# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-06 14:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('git_project', '0030_auto_20170303_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='label',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='git_project.Label'),
        ),
    ]