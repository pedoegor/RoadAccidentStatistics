# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from RoadAccidentStatistics.models import *
from utils.region_offset import RegionOffset
from django.http import HttpResponse
import json


def get_region_by_name(name):
    return Region.objects.filter(name=name)[0]


def get_region_list_for_select():
    def dfs(region, level, region_list):
        region_list.append(RegionOffset(region.name, level))
        for child in region.region_set.all():
            dfs(child, level + 1, region_list)

    regions = []
    dfs(Region.objects.filter(parent=None)[0], 0, regions)
    return regions


def render_object_hierarchy(request):

    return render_to_response('hierarchy.template.html', {'regions': get_region_list_for_select()})


def dashboard(request):
    return render_to_response('dashboard.html', {'title': u'Статистика ДТП'})


def bubble_chart(request):
    min_year = RegionStat.objects.earliest("year").year
    max_year = RegionStat.objects.latest("year").year
    return render_to_response('bubble_chart_with_form.html', {"title": u'Статистика ДТП',
                                                              "parameters_title": u'Параметры',
                                                              "info_header": u'Информация',
                                                              "regions": get_region_list_for_select(),
                                                              "years": [x for x in range(min_year, max_year + 1)]})


def bubble_chart_plot(request, regions, from_year, to_year):
    regions = regions.split(",")
    from_year = int(from_year)
    to_year = int(to_year)
    hAxis = u'Количество ДТП на 10 тыс. ед. ТС'
    vAxis = u'Число пострадавших на 100 тыс. жителей'
    chart_title = u'Количество ДТП, число пострадавших и численность населения регионов с %s по %s года' % (from_year,
                                                                                                        to_year,)
    data = [[u'Регион', hAxis, vAxis, u'Год', u'Численность населения']]
    for region_name in regions:
        region = get_region_by_name(region_name)
        for year in range(from_year, to_year + 1):
            population = RegionPopulation.objects.filter(region=region, year=year)[0].population
            crashed_number = RegionCrashedTransport.objects.filter(region=region, year=year)[0].crashed_transport_number
            hurted_number = RegionStat.objects.filter(region=region, year=year, accident_type='all')[0].get_hurted_number()
            data.append([region.name, crashed_number / (population / 10000), hurted_number / (population / 100000),
                         '%s' % (year,), population])
    return HttpResponse(json.dumps({"chart_title": chart_title,
                                    "hAxis_title": hAxis,
                                    "vAxis_title": vAxis,
                                    "chart_data": data}), content_type="application/json")


