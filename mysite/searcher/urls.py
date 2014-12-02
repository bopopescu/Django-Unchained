from django.conf.urls import patterns, url, include
from searcher import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = patterns('',
	url(r'^account/(?P<username>\S+)$', 'searcher.views.account_lookup'),

	url(r'^close-account/$', 'searcher.views.close_account_form', name='close_account'),

	url(r'^transfer/$', 'searcher.views.transfer_money_form', name='transfer_money'),

    url(r'^$', 'searcher.views.login_user'),

	url(r'^login/$', 'searcher.views.login_user'),
)
	
