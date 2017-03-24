from django.conf.urls import url
from .views import ImageDelete
from . import views

app_name = 'git_project'

urlpatterns = [
    #Home page
    url(r'^$', views.indexView.as_view(), name='index'),
    #Project detail
    url(r'^(?P<pk>[0-9]+)/$', views.detailView.as_view(), name='detail'),
    #Project create
    url(r'project/add/$', views.ProjectCreate.as_view(), name='project_add'),
    #Update Project
    url(r'project/(?P<pk>[0-9]+)/$', views.ProjectUpdate.as_view(), name='project_update'),
    #Delete Project
    url(r'project/(?P<pk>[0-9]+)/delete/$', views.ProjectDelete.as_view(), name='project_delete'),
    #Add user for project
    url(r'^(?P<pk>[0-9]+)/users/$', views.CreateRoleForUsers.as_view(), name='users_for_project'),
    #Create an issue
    url(r'project/(?P<pk>[0-9]+)/add_issue/$', views.IssueCreate.as_view(), name='issue_add'),
    #All issues
    url(r'^issues/$', views.allIssuesView.as_view(), name='all_issues'),
    # Issue detail
    url(r'issues/(?P<pk>[0-9]+)/detail/$', views.IssueDetailView.as_view(), name='issue_details'),
    #Update issue
    url(r'issues/(?P<pk>[0-9]+)/update/$', views.IssueUpdate.as_view(), name='issue_update'),
    #Login
    url(r'^login/$', views.login_view, name='login'),
    #Logout
    url(r'^logout/$', views.logout_view, name='logout'),
    #Register
    url(r'^register/$', views.register_view, name='register'),
    #User profile view
    url(r'^profile/$', views.UserProfileProjectView.as_view(), name='user_profile'),
    #Add user photo
    url(r'^profile/photo/add/$', views.CreateProfile.as_view(), name='add_photo'),
    #Update profile
    url(r'^profile/(?P<pk>[0-9]+)/update/$', views.UserProfileUpdate.as_view(), name='user_profile_update'),
    #Add comment for exact issue
    url(r'^issues/(?P<pk>[0-9]+)/detail/comment/$', views.CreateComment.as_view(), name='add_comment'),
    #Delete comment
    url(r'comment/(?P<pk>[0-9]+)/delete/$', views.CommentDelete.as_view(), name='comment_delete'),
    #Delete profile photo
    url(r'^profile/photo/(?P<pk>[0-9]+)/delete/$', views.ImageDelete.as_view(), name='delete_photo'),
    #Show commits for project ID
    url(r'project/(?P<pk>[0-9]+)/commits/$', views.ProjectCommit_detailView.as_view(), name='project_commit'),
    #Add coment
    url(r'project/(?P<pk>[0-9]+)/add_commit/$', views.CommitCreate.as_view(), name='commit_add'),
    #Commit update
    url(r'project/commit/(?P<pk>[0-9]+)/update/$', views.CommitUpdate.as_view(), name='update_commit'),
    # Add new branch
    url(r'^project/branch/add/$', views.BranchCreate.as_view(), name='add_branch'),
    #Change password
    url(r'^password/$', views.change_password, name='change_password'),
    # Redirect to search
    url(r'^search/$', views.search, name='search'),
    #Show graf for project ID
    url(r'^graph/(?P<pk>[0-9]+)/$', views.weather_chart_view, name='graph'),
]