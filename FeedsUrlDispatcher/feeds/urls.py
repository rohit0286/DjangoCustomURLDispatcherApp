from django.conf.urls import patterns, include, url

from views import HomeView

urlpatterns = patterns('',
    url(r'^(?P<action>\w{0,50})$', HomeView(), name='home')
)
