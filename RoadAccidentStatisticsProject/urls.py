from django.conf.urls import patterns, include, url
from RoadAccidentStatistics.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hierarchy/', render_object_hierarchy),
    url(r'^dashboard/', dashboard),
    url(r'^bubble_chart/regions/([\w ,]+)/from_year/(\d{4})/to_year/(\d{4})/data', bubble_chart_data),
    url(r'^bubble_chart/regions/([\w ,]+)/from_year/(\d{4})/to_year/(\d{4})', bubble_chart_url),
    url(r'^bubble_chart/', bubble_chart),

    url(r'^pie_chart/regions/([\w ,]+)/from_year/(\d{4})/to_year/(\d{4})/data', pie_chart_data),
    url(r'^pie_chart/regions/([\w ,]+)/from_year/(\d{4})/to_year/(\d{4})', pie_chart_url),
    url(r'^pie_chart/', pie_chart),

    url(r'^sankey_chart/regions/([\w ,]+)/from_year/(\d{4})/to_year/(\d{4})/data', sankey_chart_data),
    url(r'^sankey_chart/regions/([\w ,]+)/from_year/(\d{4})/to_year/(\d{4})', sankey_chart_url),
    url(r'^sankey_chart/', sankey_chart),


)
urlpatterns += staticfiles_urlpatterns()
