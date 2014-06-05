from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from django.views.decorators.csrf import csrf_exempt

from esicalendar.views import GroupListAPIView
from esicalendar.views import GroupAPIView
from esicalendar.views import UserAPIView

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/groups/(?P<pk>[0-9])', csrf_exempt(GroupAPIView.as_view())),
    url(r'^api/groups', csrf_exempt(GroupListAPIView.as_view())),
    url(r'^api/users/(?P<pk>[0-9])', csrf_exempt(UserAPIView.as_view())),
)
