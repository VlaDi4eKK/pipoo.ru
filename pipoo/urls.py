from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', "catalog.views.home"),
    url(r'^forum/', include("forum.urls")),
    url(r'^catalog/', include("catalog.urls")),
    url(r'^account/', include("account.urls")),
    url(r'^comment/', include("comments.urls")),
)
