from django.conf.urls import patterns, include, url
from RoadAccidentStatistics.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hierarchy/', render_object_hierarchy),
    url(r'^dashboard/', dashboard),
)
urlpatterns += staticfiles_urlpatterns()
