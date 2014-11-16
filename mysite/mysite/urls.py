from django.conf.urls import patterns, include, url
from django.contrib import admin

import searcher

urlpatterns = patterns('',
	url(r'^', include('searcher.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
