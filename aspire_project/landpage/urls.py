from django.conf.urls import patterns, include, url

from landpage.views import landpage
from landpage.views import forgot_password


urlpatterns = patterns('',
    url(r'^$', landpage.landpage_page, name='landpage'),
    url(r'^landpage$', landpage.landpage_page),
    url(r'^forgot_password$', forgot_password.forgot_password_page, name='forgot_password'),
    url(r'^reset_password$', forgot_password.reset_password, name='reset_password'),
    url(r'^captcha/', include('captcha.urls'))
)