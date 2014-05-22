from django.conf.urls import patterns, include, url
from RoadAccidentStatistics.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import RedirectView


urlpatterns = patterns('',
    url(r'^roadstat/(\w{2})/', dashboard),

    url(r'^roadstat/trend_chart/(\w{2})/regions/([\w ,-\\.]+)/from_year/(\d{4})/to_year/(\d{4})/chart_type/(\w+)/trend_type/(\w+)/accident_type/(\w+)/stat_type/(\w+)/scale_type/(\w+)/data', trend_chart_data),
    url(r'^roadstat/trend_chart/(\w{2})/regions/([\w ,-\\.]+)/from_year/(\d{4})/to_year/(\d{4})/chart_type/(\w+)/trend_type/(\w+)/accident_type/(\w+)/stat_type/(\w+)/scale_type/(\w+)', trend_chart_url),
    url(r'^roadstat/trend_chart/(\w{2})/', trend_chart),

    url(r'^roadstat/pie_chart/(\w{2})/regions/([\w ,-\\.]+)/stat_type/(\w+)/from_year/(\d{4})/to_year/(\d{4})/data', pie_chart_data),
    url(r'^roadstat/pie_chart/(\w{2})/regions/([\w ,-\\.]+)/stat_type/(\w+)/from_year/(\d{4})/to_year/(\d{4})', pie_chart_url),
    url(r'^roadstat/pie_chart/(\w{2})/', pie_chart),

    url(r'^roadstat/sankey_chart/(\w{2})/regions/([\w ,-\\.]+)/stat_type/(\w+)/from_year/(\d{4})/to_year/(\d{4})/data', sankey_chart_data),
    url(r'^roadstat/sankey_chart/(\w{2})/regions/([\w ,-\\.]+)/stat_type/(\w+)/from_year/(\d{4})/to_year/(\d{4})', sankey_chart_url),
    url(r'^roadstat/sankey_chart/(\w{2})/', sankey_chart),

    url(r'^roadstat/$', RedirectView.as_view(url='/roadstat/en')),

)
urlpatterns += staticfiles_urlpatterns()
