from django.conf.urls import patterns, include, url
from RoadAccidentStatistics.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import RedirectView


urlpatterns = patterns('',
    url(r'^$', dashboard),

    url(r'^trend_chart/regions/([\w ,-\\.]+)/from_year/(\d{4})/to_year/(\d{4})/chart_type/(\w+)/trend_type/(\w+)/accident_type/(\w+)/stat_type/(\w+)/scale_type/(\w+)/data', trend_chart_data),
    url(r'^trend_chart/regions/([\w ,-\\.]+)/from_year/(\d{4})/to_year/(\d{4})/chart_type/(\w+)/trend_type/(\w+)/accident_type/(\w+)/stat_type/(\w+)/scale_type/(\w+)', trend_chart_url),
    url(r'^trend_chart/', trend_chart),

    url(r'^pie_chart/regions/([\w ,-\\.]+)/stat_type/(\w+)/from_year/(\d{4})/to_year/(\d{4})/data', pie_chart_data),
    url(r'^pie_chart/regions/([\w ,-\\.]+)/stat_type/(\w+)/from_year/(\d{4})/to_year/(\d{4})', pie_chart_url),
    url(r'^pie_chart/', pie_chart),

    url(r'^sankey_chart/regions/([\w ,-\\.]+)/stat_type/(\w+)/from_year/(\d{4})/to_year/(\d{4})/data', sankey_chart_data),
    url(r'^sankey_chart/regions/([\w ,-\\.]+)/stat_type/(\w+)/from_year/(\d{4})/to_year/(\d{4})', sankey_chart_url),
    url(r'^sankey_chart/', sankey_chart),
)
urlpatterns += staticfiles_urlpatterns()
