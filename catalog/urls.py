from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', "catalog.views.home"),
    url(r'^(?P<url>[\-\w]+)/$', 'catalog.views.category_view'),
    url(r'^(?P<url_categ>[\-\w]+)/(?P<url_video>[\-\w]+)/$', 'catalog.views.video_view'),
)
