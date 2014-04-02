from django.conf.urls import patterns, include, url
from RoadAccidentStatistics.views import render_object_hierarchy
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'RoadAccidentStatisticsProject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hierarchy/', render_object_hierarchy),
)
urlpatterns += staticfiles_urlpatterns()
