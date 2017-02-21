from django.conf.urls import url
from . import views

app_name = 'git_project'

urlpatterns = [
    url(r'^$', views.indexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.detailView.as_view(), name='detail'),
    url(r'project/add/$', views.ProjectCreate.as_view(), name='project_add'),
    url(r'project/(?P<pk>[0-9]+)/$', views.ProjectUpdate.as_view(), name='project_update'),
    url(r'project/(?P<pk>[0-9]+)/delete/$', views.ProjectDelete.as_view(), name='project_delete'),

    url(r'project/(?P<pk>[0-9]+)/add_issue/$', views.IssueCreate.as_view(), name='issue_add'),

    url(r'^issues/$', views.allIssuesView.as_view(), name='all_issues'),

    url(r'^login/$', views.login_view, name='login'),

    url(r'^logout/$', views.logout_view, name='logout'),

    url(r'^register/$', views.register_view, name='register'),

    url(r'^project/add/confirm/$', views.HistoryProjectCreate.as_view(), name='confirm'),

    url(r'^profile/$', views.UserProjectView.as_view(), name='user_profile'),

    url(r'^profile/photo/$', views.CreateProfile.as_view(), name='add_photo'),
]