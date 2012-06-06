from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('main.views',
    url(r'^$', 'index',name = 'main'),
    url(r'^test/$', 'test',name = 'test'),        
)

