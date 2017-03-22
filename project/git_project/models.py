import os

from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.FileField()

    def delete(self, *args, **kwargs):
        # You have to prepare what you need before delete the model
        storage, path = self.image.storage, self.image.path
        # Delete the model before the file
        super(Profile, self).delete(*args, **kwargs)
        # Delete the file after the model
        storage.delete(path)


class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    proj_title = models.CharField(max_length=32)
    proj_desc = models.CharField(max_length=1024)
    proj_start = models.DateTimeField(default=timezone.now)
    proj_completed = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('git_project:detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.proj_title

class Label(models.Model):
    lab_name = models.CharField(max_length=32)
    lab_desc = models.CharField(max_length=512)
    lab_color =  models.CharField(max_length=32)

    def __str__(self):
        return self.lab_name

class Issue(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, default=0)
    label = models.ForeignKey(Label, on_delete=models.CASCADE, default=1)
    issue_title = models.CharField(max_length=32)
    issue_desc = models.CharField(max_length=1024)
    issue_opened = models.BooleanField(default=True)
    issue_completed = models.IntegerField(default=0)
    issue_startdate = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.issue_title

class RoleHistory(models.Model):
    role_name = models.CharField(max_length=32)

    def __str__(self):
        return self.role_name

class Role(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    role_history = models.ForeignKey(RoleHistory, on_delete=models.CASCADE)

class Branch(models.Model):
    branch_name = models.CharField(max_length=32)
    branch_desc = models.CharField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.branch_name



class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, default=0)
    comment_body = models.CharField(max_length=4096)
    comment_date = models.DateTimeField(default=timezone.now)

class Commit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, default=0)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, default=0)
    commit_title = models.CharField(max_length=64)
    commit_body = models.CharField(max_length=16384)
    commit_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.commit_title




















