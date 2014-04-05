# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from RoadAccidentStatistics.models import *
from utils.wrap_classes import *
from utils.chart_support_types import *
from django.http import HttpResponse
from django.views.defaults import bad_request
import json


def stringify_list(array):
    return '%s' % (', '.join(str(x) for x in array))


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
    return render_to_response('dashboard.html', {'type': 'dashboard', 'title': u'Статистика ДТП'})


def bubble_chart(request):
    min_year = RegionStat.objects.earliest("year").year
    max_year = RegionStat.objects.latest("year").year
    return render_to_response('bubble_chart_with_form.html', {"type": "bubble_chart",
                                                              "title": u'Статистика ДТП',
                                                              "chart_title": u'Пузырьковая диаграмма',
                                                              "parameters_title": u'Параметры',
                                                              "info_header": u'Информация',
                                                              "regions": get_region_list_for_select(),
                                                              "years": [x for x in range(min_year, max_year + 1)]})


def bubble_chart_url(request, regions, from_year, to_year):
    regions = regions.split(",")
    parameters = ((u'Регионы', stringify_list(regions)), (u'С', from_year), (u'По', to_year),)
    return render_to_response('bubble_chart_by_url.html', {"type": "bubble_chart",
                                                           "title": u'Статистика ДТП',
                                                           "chart_title": u'Пузырьковая диаграмма',
                                                           "parameters_title": u'Параметры',
                                                           "info_header": u'Информация',
                                                           "parameters": parameters,
                                                           "url": request.path})


def bubble_chart_data(request, regions, from_year, to_year):
    regions = regions.split(",")
    from_year = int(from_year)
    to_year = int(to_year)
    xAxis = u'Количество ДТП на 10 тыс. ед. ТС'
    yAxis = u'Число пострадавших на 100 тыс. жителей'
    chart_title = u'Количество ДТП, число пострадавших и численность населения регионов с %s по %s года' % (from_year,
                                                                                                        to_year,)
    data = [[u'Регион', xAxis, yAxis, u'Год', u'Численность населения']]
    for region_name in regions:
        region = get_region_by_name(region_name)
        for year in range(from_year, to_year + 1):
            population = RegionPopulation.objects.filter(region=region, year=year)[0].population
            crashed_number = RegionCrashedTransport.objects.filter(region=region, year=year)[0].crashed_transport_number
            hurt_number = RegionStat.objects.filter(region=region, year=year, accident_type='all')[0].get_hurt_number('all')
            data.append([region.name, crashed_number / (population / 10000), hurt_number / (population / 100000),
                         '%s' % (year,), population])
    return HttpResponse(json.dumps({"chart_title": chart_title,
                                    "xAxis_title": xAxis,
                                    "yAxis_title": yAxis,
                                    "chart_data": data}), content_type="application/json")


def trend_chart(request):
    min_year = RegionStat.objects.earliest("year").year
    max_year = RegionStat.objects.latest("year").year
    return render_to_response('trend_chart_with_form.html', {"type": "trend_chart",
                                                              "title": u'Статистика ДТП',
                                                              "chart_title": u'График статистики ДТП с трендом',
                                                              "parameters_title": u'Параметры',
                                                              "info_header": u'Информация',
                                                              "regions": get_region_list_for_select(),
                                                              "years": [x for x in range(min_year, max_year + 1)],
                                                              "accident_types": accident_types,
                                                              "hurt_types": hurt_types,
                                                              "chart_types": chart_types,
                                                              "trend_types": trend_types})


def trend_chart_url(request, regions, from_year, to_year, chart_type, trend_type, accident_type, hurt_type):
    regions = regions.split(",")
    from_year = int(from_year)
    to_year = int(to_year)
    accident_name = get_accident_name_by_type(accident_type)
    hurt_name = get_hurt_name_by_type(hurt_type)
    chart_name = get_chart_name_by_type(chart_type)
    trend_name = get_trend_name_by_type(trend_type)

    if from_year > to_year or accident_name is None or hurt_name is None or chart_name is None or trend_name is None:
        return bad_request(request)

    parameters = ((u'Регионы', stringify_list(regions)), (u'С', from_year), (u'По', to_year), (u'Тип графика', chart_name),
                  (u'Линия тренда', trend_name), (u'Причина ДТП', accident_name), (u'Наблюдаемая величина', hurt_name))
    return render_to_response('trend_chart_by_url.html', {"type": "trend_chart",
                                                          "title": u'Статистика ДТП',
                                                          "chart_title": u'График статистики ДТП с трендом',
                                                          "parameters_title": u'Параметры',
                                                          "info_header": u'Информация',
                                                          "parameters": parameters,
                                                          "url": request.path})


def trend_chart_data(request, regions, from_year, to_year, chart_type, trend_type, accident_type, hurt_type):
    regions = regions.split(",")
    from_year = int(from_year)
    to_year = int(to_year)
    accident_name = get_accident_name_by_type(accident_type)
    hurt_name = get_hurt_name_by_type(hurt_type)
    chart_name = get_chart_name_by_type(chart_type)
    trend_name = get_trend_name_by_type(trend_type)

    if from_year > to_year or accident_name is None or hurt_name is None or chart_name is None or trend_name is None:
        return None

    xAxis = u'Год'
    yAxis = hurt_name
    chart_title = u'%s по причине \"%s\" с %s по %s года' % (hurt_name, accident_name, from_year,to_year,)
    year_value_type_function = lambda x: x if chart_type == "point" or trend_type != 'no' else str(x)
    data = [[u'Год'] + regions] + [[year_value_type_function(year)] for year in range(from_year, to_year + 1)]

    stat_data = RegionStat.objects.filter(accident_type=accident_type)
    for region_name in regions:
        region_stat_data = stat_data.filter(region=get_region_by_name(region_name))
        for i in range(to_year + 1 - from_year):
            data[i + 1].append(region_stat_data.filter(year=from_year + i)[0].get_hurt_number(hurt_type))

    return HttpResponse(json.dumps({"chart_title": chart_title,
                                    "xAxis_title": xAxis,
                                    "yAxis_title": yAxis,
                                    "chart_data": data,
                                    "chart_type": chart_type,
                                    "trend_type": trend_type}), content_type="application/json")

