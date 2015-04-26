from django.conf.urls import patterns, include, url
from .import views
from django.contrib import admin

urlpatterns = patterns('',
	url(r'^$', views.post_list),
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail),
	url(r'^admin/', include(admin.site.urls)),
	#url(r'', include('django.contrib.flatpages.urls')),
	
	)
