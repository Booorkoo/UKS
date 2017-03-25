import time, datetime
from datetime import datetime
from django.contrib.auth.forms import PasswordChangeForm
from django.core.checks import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Project, Issue, Label,  Profile, Comment, Role, Commit, Branch, Profile
from django.core.urlresolvers import reverse_lazy, reverse
from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from .forms import UserForm, UserRegisterForm
from django.contrib.auth.models import User
from chartit import Chart, DataPool

#View for home page
class indexView(generic.ListView):
    template_name = 'layout/index.html'
    context_object_name = 'all_projects'

    def get_queryset(self):
        return Project.objects.all()

#View for user profile project
class UserProfileProjectView(generic.ListView):
    template_name = 'layout/user_profile.html'
    context_object_name = 'all_user_projects'

    def get_queryset(self):
        return Project.objects.all()

#View for detail
class detailView(generic.DetailView):
    template_name = 'layout/detail.html'
    model = Project

    def get_context_data(self, **kwargs):

        context = super(detailView, self).get_context_data(**kwargs)
        context["all_roles"] = Role.objects.all()
        return context

#View for project commit detail
class ProjectCommit_detailView(generic.DetailView):
    template_name = 'layout/project_commit_detail.html'
    model = Project

    def get_context_data(self, **kwargs):

        context = super(ProjectCommit_detailView, self).get_context_data(**kwargs)
        context["all_branches"] = Branch.objects.all()
        return context

#View for commit create
class CommitCreate(CreateView):
    template_name = 'layout/project_commit_detail.html'
    model = Commit
    fields = ['user', 'project', 'branch', 'commit_title', 'commit_body']
    #success_url = reverse_lazy('git_project:index')
    def __init__(self, **kwargs):
        super(CommitCreate, self).__init__(**kwargs)
        self.request = None

    def get_success_url(self):
        # Redirect to previous url
        return self.request.META.get('HTTP_REFERER', None)

#View for create project
class ProjectCreate(CreateView):
    template_name = 'layout/project_form.html'
    model = Project

    fields = ['user', 'proj_title', 'proj_desc', 'proj_completed']
    success_url = reverse_lazy('git_project:user_profile')

#View for project update
class ProjectUpdate(UpdateView):
    template_name = 'layout/project_update_form.html'
    model = Project
    fields = ['proj_desc', 'proj_completed']
#View for delete project
class ProjectDelete(DeleteView):
    template_name = 'layout/project_form.html'
    model = Project
    #success_url = reverse_lazy('git_project:index')

    def __init__(self, **kwargs):
        super(ProjectDelete,self).__init__(**kwargs)
        self.request = None

    def get_success_url(self):
        # Redirect to previous url
        return self.request.META.get('HTTP_REFERER', None)

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
    return redirect('git_project:index')

#View for create issue
class IssueCreate(CreateView):
    template_name = 'layout/detail.html'
    model = Issue
    fields = ['project', 'issue_title', 'issue_desc', 'issue_opened', 'issue_completed']
    #success_url = reverse_lazy('git_project:index')

    def __init__(self, **kwargs):
        super(IssueCreate, self).__init__(**kwargs)
        self.request = None

    def get_success_url(self):
        # Redirect to previous url
        return self.request.META.get('HTTP_REFERER', None)

#View for update issue
class IssueUpdate(UpdateView):
    template_name = 'layout/issue_detail.html'
    model = Issue
    fields = ['issue_title', 'issue_desc', 'issue_opened', 'issue_completed']
    #success_url = reverse_lazy('git_project:user_profile')

    def __init__(self, **kwargs):
        super(IssueUpdate, self).__init__(**kwargs)
        self.request = None

    def get_success_url(self):
        # Redirect to previous url
        return self.request.META.get('HTTP_REFERER', None)


#View for all issues view
class allIssuesView(generic.ListView):
    template_name = 'layout/all_issues.html'
    context_object_name = 'all_issues'

    def get_queryset(self):
        return Issue.objects.all()
#View for issues detail
class IssueDetailView(generic.DetailView):
    template_name = 'layout/issue_detail.html'
    model = Issue

    def get_context_data(self, **kwargs):
        context = super(IssueDetailView, self).get_context_data(**kwargs)
        context["all_comments"] = Comment.objects.all()
        return context

#View for create profile
class CreateProfile(CreateView):
    template_name = 'layout/add_photo.html'
    model = Profile
    fields = ['user', 'image']
    success_url = reverse_lazy('git_project:index')

#View for user profil update
class UserProfileUpdate(UpdateView):
    template_name = 'layout/user_profile_update.html'
    model = User
    fields = ['first_name', 'last_name', 'username', 'email']
    success_url = reverse_lazy('git_project:user_profile')

#View for list comments
class CommentListView(generic.ListView):
    template_name = 'layout/add_comment.html'
    context_object_name = 'all_comments'

    def get_queryset(self):
        return Comment.objects.all()
#View for create coment
class CreateComment(CreateView):
    template_name = 'layout/issue_detail.html'
    model = Comment
    fields = ['comment_body', 'issue', 'user']
    #success_url = reverse_lazy('git_project:all_issues')

    def __init__(self, **kwargs):
        super(CreateComment, self).__init__(**kwargs)
        self.request = None

    def get_success_url(self):
        # Redirect to previous url
        return self.request.META.get('HTTP_REFERER', None)
#View for coment delete
class CommentDelete(DeleteView):
    template_name = 'layout/issue_detail.html'
    model = Comment
    #success_url = reverse_lazy('git_project:index')

    def __init__(self, **kwargs):
        super(CommentDelete, self).__init__(**kwargs)
        self.request = None

    def get_success_url(self):
        # Redirect to previous url
        return self.request.META.get('HTTP_REFERER', None)


#View for create role for users
class CreateRoleForUsers(CreateView):
    template_name = 'layout/add_role_for_user.html'
    model = Role
    fields = ['user', 'project', 'role_history']
    success_url = reverse_lazy('git_project:user_profile')


#View for delete image
class ImageDelete(DeleteView):
    template_name = 'layout/delete_photo.html'
    model = Profile
    success_url = reverse_lazy('git_project:index')


#View for create branch
class BranchCreate(CreateView):
    template_name = 'layout/create_branch.html'
    model = Branch
    fields = ['branch_name', 'branch_desc']
    success_url = reverse_lazy('git_project:index')

#View for update commit
class CommitUpdate(UpdateView):
    template_name = 'layout/update_commit.html'
    model = Commit
    def get_context_data(self, **kwargs):
        context = super(CommitUpdate, self).get_context_data(**kwargs)
        context["all_branches"] = Branch.objects.all()
        return context
    fields = ['commit_title', 'commit_body', 'branch']
    success_url = reverse_lazy('git_project:user_profile')

#View for change password
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request,('Your password was successfully updated!'))
            return redirect('git_project:index')
        else:
            messages.error(request,('Please correct the error below.'))
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'layout/change_password.html', {
        'form': form
})
#View for search
def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        proj = Project.objects.filter(proj_title__icontains=q)
        return render(request, 'layout/search_results.html', {'proj': proj, 'query': q})
    else:
        return HttpResponse('Please submit a search term.')



#view for chart
def chart_view(request, pk):
    #Step 1: Create a DataPool with the data we want to retrieve.
    commit_data = \
        DataPool(
           series=
            [{'options': {
               'source': Commit.objects.order_by('-commit_date')},
              'terms': [
                ('commit_date', lambda d: time.mktime(d.timetuple())),
                'commit_title',
                'project',
                'user',
                'branch']}
             ])

    #Step 2: Create the Chart object
    cht = Chart(
            datasource = commit_data,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'commit_date': [
                    'project',
                    'user',
                    'branch']
                  }}],
            chart_options =
              {'title': {
                   'text': 'Project chart'},
               'xAxis': {
                    'title': {
                       'text': 'DATE'}},
               'yAxis': {
                    'title': {
                        'text': 'User/Project/Branch' }}},
    x_sortf_mapf_mts = (None, lambda i: datetime.fromtimestamp(i).strftime("%Y-%m-%d, %H:%M"), False))
    #Step 3: Send the chart object to the template.
    #render_to_response('app/graphs.html', {'issueschart': cht})
    return render_to_response('layout/chart.html', {'weatherchart': cht})
































