# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-01 14:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('git_project', '0004_auto_20170201_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='label',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='git_project.Label'),
        ),
    ]