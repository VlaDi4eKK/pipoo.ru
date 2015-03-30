from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # url(r'^$', "comments.views.comment"),
    url(r'(?P<url_categ>[\-\w]+)/(?P<url_video>[\-\w]+)/$', 'comments.views.comment')

)