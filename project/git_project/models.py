from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.FileField()

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
    label = models.ForeignKey(Label, on_delete=models.CASCADE, default=0)
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

#class User(models.Model):
    #role = models.ForeignKey(Role, on_delete=models.CASCADE, default=0)
    #user_lastname = models.CharField(max_length=32)
    #user_username = models.CharField(max_length=32)
    #user_password = models.CharField(max_length=32)

class ProjectHistory(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    user_start_date = models.DateTimeField(default=timezone.now)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, default=0)
    comment_body = models.CharField(max_length=4096)
    comment_date = models.DateTimeField(default=timezone.now)

class Commit(models.Model):
    commit_link = models.URLField(default="")
    commit_date = models.DateTimeField(default=timezone.now)

class IssueChange(models.Model):
    property_name = models.CharField(max_length=32)
    old_value = models.CharField(max_length=32)
    new_value = models.CharField(max_length=32)

class HistoryItem(models.Model):
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, default=0)
    issue_change = models.ForeignKey(IssueChange, on_delete=models.CASCADE, default=0)
    commit = models.ForeignKey(Commit, on_delete=models.CASCADE, default=0)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    date_time = models.DateTimeField(default=timezone.now)


















