# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-01 20:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('git_project', '0006_auto_20170201_1548'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_body', models.CharField(max_length=512)),
                ('comment_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Commit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commit_link', models.URLField(default='')),
                ('commit_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='HistoryItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('comment', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='git_project.Comment')),
                ('commit', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='git_project.Commit')),
                ('issue', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='git_project.Issue')),
            ],
        ),
        migrations.CreateModel(
            name='IssueChange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_name', models.CharField(max_length=32)),
                ('old_value', models.CharField(max_length=32)),
                ('new_value', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('project', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='git_project.Project')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_name', models.CharField(max_length=32)),
                ('role_desc', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=32)),
                ('user_lastname', models.CharField(max_length=32)),
                ('user_username', models.CharField(max_length=32)),
                ('user_password', models.CharField(max_length=32)),
                ('role', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='git_project.Role')),
            ],
        ),
        migrations.AddField(
            model_name='projecthistory',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='git_project.User'),
        ),
        migrations.AddField(
            model_name='historyitem',
            name='issue_change',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='git_project.IssueChange'),
        ),
        migrations.AddField(
            model_name='historyitem',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='git_project.User'),
        ),
    ]
