# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from django.views.decorators.csrf import csrf_exempt

from core.views import HomeView
from core.views import SignUpView

from core.views import GroupListAPIView
from core.views import GroupAPIView
from core.views import GroupSubjectsAPIView
from core.views import UserAPIView
from core.views import UserGroupsAPIView
from core.views import UserPrivateAPIView
from core.views import SignUpAPIView

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view()),
    url(r'^signup', SignUpView.as_view()),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/groups/(?P<pk>[0-9])/subjects',
        csrf_exempt(GroupSubjectsAPIView.as_view())),
    url(r'^api/groups/(?P<pk>[0-9])', csrf_exempt(GroupAPIView.as_view())),
    url(r'^api/groups', csrf_exempt(GroupListAPIView.as_view())),
    url(r'^api/users/(?P<username>\w+)/private',
        csrf_exempt(UserPrivateAPIView.as_view())),
    url(r'^api/users/(?P<username>\w+)/groups',
        csrf_exempt(UserGroupsAPIView.as_view())),
    url(r'^api/users/(?P<username>\w+)', csrf_exempt(UserAPIView.as_view())),
    url(r'^api/signup', csrf_exempt(SignUpAPIView.as_view()))
)
