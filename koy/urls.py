from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'koy.views.home', name='home'),
    url(r'', include('blog.urls')),
	#url(r'^admin/', include(admin.site.urls)),
)
