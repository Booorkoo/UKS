# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-29 17:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('git_project', '0003_issue_label'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comm_body', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='Commit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commit_link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='HistoryItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField()),
                ('user_id_hist', models.IntegerField()),
                ('issue_id', models.IntegerField()),
                ('comment_id', models.IntegerField()),
                ('commit_id', models.IntegerField()),
                ('issue_change_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='IssueChange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_name', models.CharField(max_length=64)),
                ('old_value', models.CharField(max_length=128)),
                ('new_value', models.CharField(max_length=128)),
            ],
        ),
    ]
