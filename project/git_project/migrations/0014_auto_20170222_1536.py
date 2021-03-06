# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-22 14:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('git_project', '0013_auto_20170221_1616'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='issue',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='git_project.Issue'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_body',
            field=models.CharField(max_length=4096),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.FileField(default=0, upload_to=''),
        ),
    ]
