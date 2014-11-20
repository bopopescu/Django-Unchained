from django.conf.urls import patterns, url, include
from searcher import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = patterns('',
	url(r'^account/(?P<barcode>\S+)$', 'searcher.views.account_lookup'),
    url(r'^$', 'searcher.views.login_user'),
	url(r'^login/$', 'searcher.views.login_user'),
)

