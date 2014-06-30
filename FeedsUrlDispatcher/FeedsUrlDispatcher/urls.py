from django.conf.urls import patterns, include, url

from feeds import urls as f_urls
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'FeedsUrlDispatcher.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^feeds/', include(f_urls)),
)
