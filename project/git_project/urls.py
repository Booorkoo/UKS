from django.conf.urls import url

from .views import ImageDelete
from . import views

app_name = 'git_project'

urlpatterns = [
    url(r'^$', views.indexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.detailView.as_view(), name='detail'),
    url(r'project/add/$', views.ProjectCreate.as_view(), name='project_add'),
    url(r'project/(?P<pk>[0-9]+)/$', views.ProjectUpdate.as_view(), name='project_update'),
    url(r'project/(?P<pk>[0-9]+)/delete/$', views.ProjectDelete.as_view(), name='project_delete'),

    #dodela korisnika projektu
    url(r'^(?P<pk>[0-9]+)/users/$', views.CreateRoleForUsers.as_view(), name='users_for_project'),

    url(r'project/(?P<pk>[0-9]+)/add_issue/$', views.IssueCreate.as_view(), name='issue_add'),

    url(r'^issues/$', views.allIssuesView.as_view(), name='all_issues'),

    url(r'issues/(?P<pk>[0-9]+)/detail/$', views.IssueDetailView.as_view(), name='issue_details'),

    url(r'^login/$', views.login_view, name='login'),

    url(r'^logout/$', views.logout_view, name='logout'),

    url(r'^register/$', views.register_view, name='register'),

    #url(r'^project/add/confirm/$', views.HistoryProjectCreate.as_view(), name='confirm'),

    url(r'^profile/$', views.UserProfileProjectView.as_view(), name='user_profile'),

    url(r'^profile/photo/add/$', views.CreateProfile.as_view(), name='add_photo'),

    url(r'^profile/(?P<pk>[0-9]+)/update/$', views.UserProfileUpdate.as_view(), name='user_profile_update'),

    #izlistavanje komentara
    #url(r'^issues/(?P<pk>[0-9]+)/comment/$', views.CommentListView.as_view(), name='all_comments'),

    url(r'^issues/(?P<pk>[0-9]+)/detail/comment/$', views.CreateComment.as_view(), name='add_comment'),

    url(r'^profile/photo/(?P<pk>[0-9]+)/delete/$', views.ImageDelete.as_view(), name='delete_photo'),
]