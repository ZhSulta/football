from django.conf.urls.defaults import patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('poll.views',
    url(r'^vote/(?P<poll_pk>\d)/$', 'vote', name='poll_ajax_vote'),
    url(r'^poll/(?P<poll_pk>\d)/$', 'poll', name='poll'),
    url(r'^result/(?P<poll_pk>\d)/$', 'result', name='poll_result'),
)

urlpatterns += staticfiles_urlpatterns()
