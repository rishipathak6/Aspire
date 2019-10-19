from django.conf.urls import patterns, include, url
from account.views import profile
from account.views import setting

urlpatterns = patterns('',
    url(r'^profile$', profile.profile_page),
    url(r'^update_user$', profile.update_user),
    url(r'^settings$', setting.settings_page),
    url(r'^update_password$', setting.update_password)
)