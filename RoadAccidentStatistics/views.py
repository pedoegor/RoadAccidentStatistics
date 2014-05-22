# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from RoadAccidentStatistics.models import *
from utils.wrap_classes import *
from utils.chart_support_types import *
from utils.elements_information import *
from django.http import HttpResponse
from django.views.defaults import bad_request
import json


def list_to_str(array):
    return u'%s' % (', '.join(x for x in array))


def get_region_by_name(name):
    if name is None:
        return None
    return Region.objects.filter(name=name)[0]


def get_region_list_for_select():
    def dfs(region, level, region_list):
        region_list.append(RegionOffset(region.name, level))
        for child in region.region_set.all():
            dfs(child, level + 1, region_list)

    regions = []
    dfs(Region.objects.filter(name=u'Российская Федерация')[0], 0, regions)
    return regions


def dashboard(request):
    return render_to_response('dashboard.html', {'type': '',
                                                'title': element['title']['label'],
                                                'lang': 'ru'})


def trend_chart(request):
    min_year = RegionStat.objects.earliest("year").year
    max_year = RegionStat.objects.latest("year").year
    return render_to_response('trend_chart_with_form.html', {"type": "trend_chart",
                                                             "title": element['title']['label'],
                                                             "chart_title": element['trend_chart_title']['label'],
                                                             'lang': 'ru',
                                                             "parameters_title": element['parameters_title']['label'],
                                                             "info_header": element['information_header']['label'],
                                                             "regions": get_region_list_for_select(),
                                                             "from_year": min_year,
                                                             "to_year": max_year,
                                                             "accident_types": accident_types,
                                                             "stat_types": stat_types,
                                                             "chart_types": chart_types,
                                                             "trend_types": trend_types,
                                                             "scale_types": scale_types})


def trend_chart_url(request, regions, from_year, to_year, chart_type, trend_type, accident_type, stat_type, scale_type):
    regions = regions.split(",")
    from_year = int(from_year)
    to_year = int(to_year)
    accident_name = get_accident_name_by_type(accident_type)
    stat_name = get_stat_name_by_type(stat_type)
    chart_name = get_chart_name_by_type(chart_type)
    trend_name = get_trend_name_by_type(trend_type)
    scale_name = get_scale_name_by_type(scale_type)

    if from_year > to_year or accident_name is None or stat_name is None or chart_name is None or trend_name is None \
            or scale_name is None:
        return bad_request(request)

    parameters = ((element['regions_title']['label'], list_to_str(regions)),
                  (element['from_title']['label'], from_year),
                  (element['to_title']['label'], to_year),
                  (element['graph_type_title']['label'], chart_name),
                  (element['trend_line_title']['label'], trend_name),
                  (element['reason_title']['label'], accident_name),
                  (element['observed_title']['label'], stat_name),
                  (element['scale_title']['label'], scale_name),)
    return render_to_response('trend_chart_by_url.html', {"type": "trend_chart",
                                                          "title": element['title']['label'],
                                                          "chart_title": element['trend_chart_title']['label'],
                                                          'lang': 'ru',
                                                          "parameters_title": element['parameters_title']['label'],
                                                          "info_header": element['information_header']['label'],
                                                          "parameters": parameters,
                                                          "url": request.path})


def trend_chart_data(request, regions, from_year, to_year, chart_type, trend_type, accident_type, stat_type,
                     scale_type):
    regions = regions.split(",")
    from_year = int(from_year)
    to_year = int(to_year)
    accident_name = get_accident_name_by_type(accident_type)
    stat_name = get_stat_name_by_type(stat_type)
    chart_name = get_chart_name_by_type(chart_type)
    trend_name = get_trend_name_by_type(trend_type)
    scale_name = get_scale_name_by_type(scale_type)

    if from_year > to_year or accident_name is None or stat_name is None or chart_name is None or trend_name is None \
            or scale_name is None:
        return None

    xAxis = element['year_title']['label']
    yAxis = stat_name
    chart_title = element['trend_reason_title']['label']  % (
        stat_name, scale_name, accident_name, from_year, to_year,)
    year_value_type_function = lambda x: x if chart_type == "point" or trend_type != 'no' else str(x)
    data = [[element['year_title']['label']] + regions] + [[year_value_type_function(year)] for year in range(from_year, to_year + 1)]

    stat_data = RegionStat.objects.filter(accident_type=accident_type)
    if scale_type == 'no':
        scale_function = lambda r, y: 1
    elif scale_type == 'population':
        scale_function = lambda r, y: RegionPopulation.objects.filter(region=r, year=y)[0].population / 100000
    else:
        scale_function = lambda r, y: RegionCrashedTransport.objects.filter(region=r, year=y)[0].crashed_transport_number / 10000

    for region_name in regions:
        region = get_region_by_name(region_name)
        region_stat_data = stat_data.filter(region=region)
        for i in range(to_year + 1 - from_year):
            try:
                data[i + 1].append(
                    region_stat_data.filter(year=from_year + i)[0].get_stat_number(stat_type) / scale_function(region, from_year + i))
            except ArithmeticError:
                data[i + 1].append(0)
    return HttpResponse(json.dumps({"chart_title": chart_title,
                                    "xAxis_title": xAxis,
                                    "yAxis_title": yAxis,
                                    "chart_data": data,
                                    "chart_type": chart_type,
                                    "trend_type": trend_type}), content_type="application/json")


def pie_chart(request):
    min_year = RegionStat.objects.earliest("year").year
    max_year = RegionStat.objects.latest("year").year
    return render_to_response('pie_chart_with_form.html', {"type": "pie_chart",
                                                           "title": element['title']['label'],
                                                           "chart_title": element['pie_chart_title']['label'],
                                                           'lang': 'ru',
                                                           "parameters_title": element['parameters_title']['label'],
                                                           "info_header": element['information_header']['label'],
                                                           "regions": get_region_list_for_select(),
                                                           "stat_types": stat_types,
                                                           "from_year": min_year,
                                                           "to_year": max_year})


def pie_chart_url(request, regions, stat_type, from_year, to_year):
    stat_name = get_stat_name_by_type(stat_type)
    parameters = [(element['regions_title']['label'], regions),
                  (element['observed_title']['label'], stat_name),
                  (element['from_title']['label'], from_year),
                  (element['to_title']['label'], to_year)]
    return render_to_response('pie_chart_by_url.html', {"type": "pie_chart",
                                                        "title": element['title']['label'],
                                                        "chart_title": element['pie_chart_title']['label'],
                                                        'lang': 'ru',
                                                        "parameters_title": element['parameters_title']['label'],
                                                        "info_header": element['information_header']['label'],
                                                        "parameters": parameters,
                                                        "url": request.path})


def pie_chart_data(request, regions, stat_type, from_year, to_year):
    regions = regions.split(",")
    from_year = int(from_year)
    to_year = int(to_year)
    stat_name = get_stat_name_by_type(stat_type)
    chart_title = element['pie_chart_title_param']['label'] % (stat_name, from_year, to_year,)
    accident_number = {
        'juridical': 0,
        'physical': 0,
        'pedestrian': 0,
        'broken': 0,
        'roads': 0,
        'hidden': 0
    }
    for region_name in regions:
        region = get_region_by_name(region_name)
        for year in range(from_year, to_year + 1):
            stat_objects = RegionStat.objects.filter(region=region, year=year)
            for current in stat_objects:
                if current.accident_type in accident_number.keys():
                    accident_number[str(current.accident_type)] += current.get_stat_number(stat_type)

    data = [[element['reason_title']['label'], stat_name]] + [[get_accident_name_by_type(current),
                                                         accident_number[current]] for current in
                                                        accident_number.keys()]
    return HttpResponse(json.dumps({"chart_title": chart_title, "chart_data": data}), content_type="application/json")


def sankey_chart(request):
    min_year = RegionStat.objects.earliest("year").year
    max_year = RegionStat.objects.latest("year").year
    return render_to_response('sankey_chart_with_form.html', {"type": "sankey_chart",
                                                              "title": element['title']['label'],
                                                              "chart_title": element['sankey_chart_title']['label'],
                                                              'lang': 'ru',
                                                              "parameters_title": element['parameters_title']['label'],
                                                              "info_header": element['information_header']['label'],
                                                              "regions": get_region_list_for_select(),
                                                              "stat_types": stat_types,
                                                              "from_year": min_year,
                                                              "to_year": max_year})


def sankey_chart_url(request, regions, stat_type, from_year, to_year):
    stat_name = get_stat_name_by_type(stat_type)
    parameters = [(element['regions_title']['label'], regions),
                  (element['observed_title']['label'], stat_name),
                  (element['from_title']['label'], from_year),
                  (element['to_title']['label'], to_year)]
    return render_to_response('sankey_chart_by_url.html', {"type": "sankey_chart",
                                                           "title": element['title']['label'],
                                                           "chart_title": element['sankey_chart_title']['label'],
                                                           'lang': 'ru',
                                                           "parameters_title": element['parameters_title']['label'],
                                                           "info_header": element['information_header']['label'],
                                                           "parameters": parameters,
                                                           "url": request.path})


def sankey_chart_data(request, regions, stat_type, from_year, to_year):
    regions = regions.split(",")
    from_year = int(from_year)
    to_year = int(to_year)
    chart_title = element['sankey_title_param']['label'] % (from_year, to_year,)
    stat_name = get_stat_name_by_type(stat_type)
    accident_number = {
        'driver': 0,
        'drunk': 0,
        'juridical': 0,
        'physical': 0,
        'pedestrian': 0,
        'children': 0,
        'broken': 0,
        'roads': 0,
        'hidden': 0,
        'all': 0,
    }
    for region_name in regions:
        region = get_region_by_name(region_name)
        for year in range(from_year, to_year + 1):
            stat_objects = RegionStat.objects.filter(region=region, year=year)
            for current in stat_objects:
                accident_number[str(current.accident_type)] += current.get_stat_number(stat_type)
    all_name = get_accident_name_by_type('all')
    driver_name = get_accident_name_by_type('driver')
    broken_name = get_accident_name_by_type('broken')
    roads_name = get_accident_name_by_type('roads')
    pedestrian_name = get_accident_name_by_type('pedestrian')
    driver_and_pedestrian_name = element['driver_pedestrian_title']['label']
    data = [[element['sankey_chart_from']['label'], element['sankey_chart_to']['label'], stat_name],
            [all_name, broken_name, accident_number['broken']],
            [all_name, roads_name, accident_number['roads']],
            [all_name, driver_and_pedestrian_name, accident_number['driver'] + accident_number['pedestrian']],
            [broken_name, ' ', -1],
            [' ', '  ', -1],
            [roads_name, '   ', -1],
            ['   ', '    ', -1],
            [driver_and_pedestrian_name, driver_name, accident_number['driver']],
            [driver_and_pedestrian_name, pedestrian_name, accident_number['pedestrian']],
            [pedestrian_name, '     ', -1],
            [driver_name, get_accident_name_by_type('physical'), accident_number['physical']],
            [driver_name, get_accident_name_by_type('juridical'), accident_number['juridical']],
            [driver_name, get_accident_name_by_type('hidden'), accident_number['hidden']]]

    return HttpResponse(json.dumps({"chart_title": chart_title, "chart_data": data}), content_type="application/json")


