from django.contrib import admin
from .models import Project, Issue, Label, Commit, Profile

admin.site.register(Project)
admin.site.register(Issue)
admin.site.register(Label)
admin.site.register(Commit)
admin.site.register(Profile)
