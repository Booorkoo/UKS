# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-26 13:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('git_project', '0020_auto_20170226_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='proj_start',
            field=models.DateField(auto_now_add=True),
        ),
    ]
