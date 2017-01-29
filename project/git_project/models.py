from django.db import models
from django.utils import timezone

class Roles(models.Model):
    role_name = models.CharField(max_length=32, null=False)
    role_desc = models.CharField(max_length=128)

class User(models.Model):
    name = models.CharField(max_length=32, null=False)
    lastname = models.CharField(max_length=32, null=False)
    username = models.CharField(max_length=32, null=False)
    password = models.CharField(max_length=32, null=False)
    role_id = models.IntegerField(null=False)

class Project(models.Model):
    proj_title = models.CharField(max_length=64, null=False)
    proj_desc = models.CharField(max_length=256, null=False)
    proj_opened = models.BooleanField(null=False)
    proj_completed = models.IntegerField(default=0, null=False)

class ProjectHistory(models.Model):
    start_date = models.DateTimeField(default=timezone.now)
    user_id = models.IntegerField(null=False)
    project_id = models.IntegerField(null=False)

class Label(models.Model):
    lab_name = models.CharField(max_length=32, null=False)
    lab_desc = models.CharField(max_length=128, null=False)
    lab_color = models.CharField(max_length=32, null=False)

class Issue(models.Model):
    issue_title = models.CharField(max_length=64, null=False)
    issue_desc = models.CharField(max_length=256, null=False)
    issue_opened = models.BooleanField(null=False)
    issue_completed = models.IntegerField(default=0, null=False)
    issue_start_date = models.DateTimeField(default=timezone.now)
    proj_id_issue = models.IntegerField(null=False)
    label_id = models.IntegerField(null=False)

class Comment(models.Model):
    comm_body = models.CharField(max_length=1024, null=False)

class Commit(models.Model):
    commit_link = models.URLField(null=False)

class IssueChange(models.Model):
    property_name = models.CharField(max_length=64)
    old_value = models.CharField(max_length=128)
    new_value = models.CharField(max_length=128)

class HistoryItem(models.Model):
    date_time = models.DateTimeField()
    user_id_hist = models.IntegerField(null=False)
    issue_id = models.IntegerField(null=False)
    comment_id = models.IntegerField(null=False)
    commit_id = models.IntegerField(null=False)
    issue_change_id = models.IntegerField(null=False)

