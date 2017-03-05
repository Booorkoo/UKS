from django.http import HttpResponseRedirect
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Project, Issue, Label,  Profile, ProjectHistory, Comment, Role
from django.core.urlresolvers import reverse_lazy, reverse
from pip._vendor.requests import delete

from .models import Project, Issue, Label,  Profile, ProjectHistory
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from .forms import UserForm, UserRegisterForm
from django.contrib.auth.models import User
from django.contrib import auth


class indexView(generic.ListView):
    template_name = 'layout/index.html'
    context_object_name = 'all_projects'

    def get_queryset(self):
        return Project.objects.all()


class UserProfileProjectView(generic.ListView):
    template_name = 'layout/user_profile.html'
    context_object_name = 'all_user_projects'

    def get_queryset(self):
        return Project.objects.all()





#class detailView(generic.DetailView):
    #model = Project
    #template_name = 'layout/detail.html'


class detailView(generic.DetailView):
    template_name = 'layout/detail.html'
    model = Project

    def get_context_data(self, **kwargs):

        context = super(detailView, self).get_context_data(**kwargs)
        context["all_roles"] = Role.objects.all()
        return context




class ProjectCreate(CreateView):
    template_name = 'layout/project_form.html'
    model = Project

    fields = ['user', 'proj_title', 'proj_desc', 'proj_completed']
    success_url = reverse_lazy('git_project:user_profile')

class ProjectUpdate(UpdateView):
    template_name = 'layout/project_form.html'
    model = Project
    fields = ['user', 'proj_title', 'proj_desc', 'proj_completed']

class ProjectDelete(DeleteView):
    template_name = 'layout/project_form.html'
    model = Project
    success_url = reverse_lazy('git_project:index')

def login_view(request):
    title = "Login"
    form = UserForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('git_project:index')
    return render(request, "layout/registration.html", {"form":form, "title":title})

def register_view(request):
    title = "register"
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        return redirect('git_project:index')

    context = {"form": form, "title": title}
    return render(request, "layout/registration.html", context)

def logout_view(request):
    logout(request)
    return render(request, "layout/index.html", {})


class IssueCreate(CreateView):
    template_name = 'layout/issue_form.html'
    model = Issue
    fields = ['project', 'issue_title', 'issue_desc', 'issue_opened', 'issue_completed', 'label']
    success_url = reverse_lazy('git_project:index')


class allIssuesView(generic.ListView):
    template_name = 'layout/all_issues.html'
    context_object_name = 'all_issues'

    def get_queryset(self):
        return Issue.objects.all()



class IssueDetailView(generic.DetailView):
    template_name = 'layout/issue_detail.html'
    model = Issue

    def get_context_data(self, **kwargs):
        context = super(IssueDetailView, self).get_context_data(**kwargs)
        context["all_comments"] = Comment.objects.all()
        return context

#class HistoryProjectCreate(CreateView):
    #template_name = 'layout/create_proj_history.html'
    #model = ProjectHistory

    #fields = ['user', 'project', 'user_start_date']
    #success_url = reverse_lazy('git_project:index')


#class UserProjectView(generic.ListView):
    #template_name = 'layout/user_profile.html'
    #context_object_name = 'userproject'

    #def get_queryset(self):
        #return ProjectHistory.objects.all()

class CreateProfile(CreateView):
    template_name = 'layout/add_photo.html'
    model = Profile
    fields = ['user', 'image']
    success_url = reverse_lazy('git_project:index')


class UserProfileUpdate(UpdateView):
    template_name = 'layout/user_profile_update.html'
    model = User
    fields = ['first_name', 'last_name', 'username', 'email']
    success_url = reverse_lazy('git_project:user_profile')


class CommentListView(generic.ListView):
    template_name = 'layout/add_comment.html'
    context_object_name = 'all_comments'

    def get_queryset(self):
        return Comment.objects.all()

class CreateComment(CreateView):
    template_name = 'layout/issue_detail.html'
    model = Comment
    fields = ['comment_body', 'issue', 'user']
    success_url = reverse_lazy('git_project:all_issues')



class CreateRoleForUsers(CreateView):
    template_name = 'layout/add_role_for_user.html'
    model = Role
    fields = ['user', 'project', 'role_history']
    success_url = reverse_lazy('git_project:index')



class ImageDelete(DeleteView):
    template_name = 'layout/delete_photo.html'
    model = Profile
    success_url = reverse_lazy('git_project:index')




































