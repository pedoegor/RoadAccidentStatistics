from django.conf.urls import patterns, include, url
from RoadAccidentStatistics.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^dashboard/(\w{2})', dashboard),
    url(r'^dashboard/', dashboard_default),
    url(r'^bubble_chart/(\w{2})/regions/([\w ,-\\.]+)/from_year/(\d{4})/to_year/(\d{4})/data', bubble_chart_data),
    url(r'^bubble_chart/(\w{2})/regions/([\w ,-\\.]+)/from_year/(\d{4})/to_year/(\d{4})', bubble_chart_url),
    url(r'^bubble_chart/(\w{2})/', bubble_chart),

    url(r'^trend_chart/(\w{2})/regions/([\w ,-\\.]+)/from_year/(\d{4})/to_year/(\d{4})/chart_type/(\w+)/trend_type/(\w+)/accident_type/(\w+)/stat_type/(\w+)/scale_type/(\w+)/data', trend_chart_data),
    url(r'^trend_chart/(\w{2})/regions/([\w ,-\\.]+)/from_year/(\d{4})/to_year/(\d{4})/chart_type/(\w+)/trend_type/(\w+)/accident_type/(\w+)/stat_type/(\w+)/scale_type/(\w+)', trend_chart_url),
    url(r'^trend_chart/(\w{2})/', trend_chart),

    url(r'^pie_chart/regions/([\w ,-\\.]+)/stat_type/(\w+)/from_year/(\d{4})/to_year/(\d{4})/data', pie_chart_data),
    url(r'^pie_chart/regions/([\w ,-\\.]+)/stat_type/(\w+)/from_year/(\d{4})/to_year/(\d{4})', pie_chart_url),
    url(r'^pie_chart/', pie_chart),

    url(r'^sankey_chart/regions/([\w ,-\\.]+)/stat_type/(\w+)/from_year/(\d{4})/to_year/(\d{4})/data', sankey_chart_data),
    url(r'^sankey_chart/regions/([\w ,-\\.]+)/stat_type/(\w+)/from_year/(\d{4})/to_year/(\d{4})', sankey_chart_url),
    url(r'^sankey_chart/', sankey_chart),

    url(r'^finland_comp/regions/([\w ,-\\.]+)/from_year/(\d{4})/to_year/(\d{4})/chart_type/(\w+)/trend_type/(\w+)/stat_type/(\w+)/scale_type/(\w+)/data', finland_comp_data),
    url(r'^finland_comp/regions/([\w ,-\\.]+)/from_year/(\d{4})/to_year/(\d{4})/chart_type/(\w+)/trend_type/(\w+)/stat_type/(\w+)/scale_type/(\w+)', finland_comp_url),
    url(r'^finland_comp/', finland_comp),

)
urlpatterns += staticfiles_urlpatterns()
