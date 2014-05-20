from django.conf.urls import patterns, include, url
from RoadAccidentStatistics.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import RedirectView
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^roadstat/(\w{2})/', dashboard),
    url(r'^roadstat/bubble_chart/(\w{2})/regions/([\w ,-\\.]+)/from_year/(\d{4})/to_year/(\d{4})/data', bubble_chart_data),
    url(r'^roadstat/bubble_chart/(\w{2})/regions/([\w ,-\\.]+)/from_year/(\d{4})/to_year/(\d{4})', bubble_chart_url),
    url(r'^roadstat/bubble_chart/(\w{2})/', bubble_chart),

    url(r'^roadstat/trend_chart/(\w{2})/regions/([\w ,-\\.]+)/from_year/(\d{4})/to_year/(\d{4})/chart_type/(\w+)/trend_type/(\w+)/accident_type/(\w+)/stat_type/(\w+)/scale_type/(\w+)/data', trend_chart_data),
    url(r'^roadstat/trend_chart/(\w{2})/regions/([\w ,-\\.]+)/from_year/(\d{4})/to_year/(\d{4})/chart_type/(\w+)/trend_type/(\w+)/accident_type/(\w+)/stat_type/(\w+)/scale_type/(\w+)', trend_chart_url),
    url(r'^roadstat/trend_chart/(\w{2})/', trend_chart),

    url(r'^roadstat/pie_chart/(\w{2})/regions/([\w ,-\\.]+)/stat_type/(\w+)/from_year/(\d{4})/to_year/(\d{4})/data', pie_chart_data),
    url(r'^roadstat/pie_chart/(\w{2})/regions/([\w ,-\\.]+)/stat_type/(\w+)/from_year/(\d{4})/to_year/(\d{4})', pie_chart_url),
    url(r'^roadstat/pie_chart/(\w{2})/', pie_chart),

    url(r'^roadstat/sankey_chart/(\w{2})/regions/([\w ,-\\.]+)/stat_type/(\w+)/from_year/(\d{4})/to_year/(\d{4})/data', sankey_chart_data),
    url(r'^roadstat/sankey_chart/(\w{2})/regions/([\w ,-\\.]+)/stat_type/(\w+)/from_year/(\d{4})/to_year/(\d{4})', sankey_chart_url),
    url(r'^roadstat/sankey_chart/(\w{2})/', sankey_chart),

    url(r'^roadstat/finland_comp/(\w{2})/regions/([\w ,-\\.]+)/from_year/(\d{4})/to_year/(\d{4})/chart_type/(\w+)/trend_type/(\w+)/stat_type/(\w+)/scale_type/(\w+)/data', finland_comp_data),
    url(r'^roadstat/finland_comp/(\w{2})/regions/([\w ,-\\.]+)/from_year/(\d{4})/to_year/(\d{4})/chart_type/(\w+)/trend_type/(\w+)/stat_type/(\w+)/scale_type/(\w+)', finland_comp_url),
    url(r'^roadstat/finland_comp/(\w{2})/', finland_comp),
    url(r'^roadstat/$', RedirectView.as_view(url='/roadstat/en')),

)
urlpatterns += staticfiles_urlpatterns()
