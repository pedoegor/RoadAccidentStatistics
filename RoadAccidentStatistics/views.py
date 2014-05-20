# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from RoadAccidentStatistics.models import *
from utils.wrap_classes import *
from utils.chart_support_types import *
from utils.translations import *
from django.http import HttpResponse
from django.views.defaults import bad_request
import json


def list_to_str(array):
    return u'%s' % (', '.join(x for x in array))


def get_region_by_name(name):
    if name is None:
        return None
    return Region.objects.filter(name=name)[0]


def get_region_list_for_select(finland_comp=False):
    def dfs(region, level, region_list):
        region_list.append(RegionOffset(region.name, level))
        for child in region.region_set.all():
            dfs(child, level + 1, region_list)

    regions = [Region.objects.filter(name=u'Финляндия')[0]] if finland_comp else []
    dfs(Region.objects.filter(name=u'Российская Федерация')[0], 0, regions)
    return regions


def dashboard(request, lang):
    print lang
    if lang not in ['ru', 'en']:
        return bad_request(request)
    return render_to_response('dashboard.html', {'type': '',
                                                 'title': international['title'][lang],
                                                 'lang': lang})


def bubble_chart(request, lang):
    min_year = RegionStat.objects.earliest("year").year
    max_year = RegionStat.objects.latest("year").year
    return render_to_response('bubble_chart_with_form.html', {"type": "bubble_chart",
                                                              "title": international['title'][lang],
                                                              "chart_title": international['bubble_chart_title'][lang],
                                                              'lang': lang,
                                                              "parameters_title": international['parameters_title'][lang],
                                                              "info_header": international['information_header'][lang],
                                                              "regions": get_region_list_for_select(),
                                                              "from_year": min_year,
                                                              "to_year": max_year})


def bubble_chart_url(request, lang, regions, from_year, to_year):
    regions = regions.split(",")
    parameters = ((international['regions_title'][lang], list_to_str(regions)), 
                  (international['from_title'][lang], from_year), 
                  (international['to_title'][lang], to_year),)
    return render_to_response('bubble_chart_by_url.html', {"type": "bubble_chart",
                                                           "title": international['title'][lang],
                                                           "chart_title": international['bubble_chart_title'][lang],
                                                           'lang': lang,
                                                           "parameters_title":international['parameters_title'][lang],
                                                           "info_header": international['information_header'][lang],
                                                           "parameters": parameters,
                                                           "url": request.path})


def bubble_chart_data(request, lang, regions, from_year, to_year):
    regions = regions.split(",")
    from_year = int(from_year)
    to_year = int(to_year)
    xAxis = international['bubble_chart_xAxis'][lang]
    yAxis = international['bubble_chart_yAxis'][lang]
    chart_title = international['bubble_chart_header'][lang] % (from_year,  to_year,)

    data = [[international['regions_title'][lang], xAxis, yAxis, international['year_title'][lang], international['population_title'][lang]]]
    for region_name in regions:
        region = get_region_by_name(region_name)
        for year in range(from_year, to_year + 1):
            population = RegionPopulation.objects.filter(region=region, year=year)[0].population
            crashed_number = RegionCrashedTransport.objects.filter(region=region, year=year)[0].crashed_transport_number
            region_stat = RegionStat.objects.filter(region=region, year=year, accident_type='all')[0]
            scaled_p = region_stat.get_stat_number('hurt') / (population / 100000) if population > 100000 else 0
            scaled_t = region_stat.accident_number / (crashed_number / 10000) if crashed_number > 10000 else 0
            data.append([region.name,
                         scaled_t,
                         scaled_p,
                         str(year), population])
    return HttpResponse(json.dumps({"chart_title": chart_title,
                                    "xAxis_title": xAxis,
                                    "yAxis_title": yAxis,
                                    "chart_data": data}), content_type="application/json")


def trend_chart(request, lang):
    min_year = RegionStat.objects.earliest("year").year
    max_year = RegionStat.objects.latest("year").year
    return render_to_response('trend_chart_with_form.html', {"type": "trend_chart",
                                                             "title": international['title'][lang],
                                                             "chart_title": international['trend_chart_title'][lang],
                                                             'lang': lang,
                                                             "parameters_title": international['parameters_title'][lang],
                                                             "info_header": international['information_header'][lang],
                                                             "regions": get_region_list_for_select(),
                                                             "from_year": min_year,
                                                             "to_year": max_year,
                                                             "accident_types": accident_types,
                                                             "stat_types": stat_types,
                                                             "chart_types": chart_types,
                                                             "trend_types": trend_types,
                                                             "scale_types": scale_types})


def trend_chart_url(request, lang, regions, from_year, to_year, chart_type, trend_type, accident_type, stat_type, scale_type):
    regions = regions.split(",")
    from_year = int(from_year)
    to_year = int(to_year)
    accident_name = get_accident_name_by_type(accident_type, lang)
    stat_name = get_stat_name_by_type(stat_type, lang)
    chart_name = get_chart_name_by_type(chart_type, lang)
    trend_name = get_trend_name_by_type(trend_type, lang)
    scale_name = get_scale_name_by_type(scale_type, lang)

    if from_year > to_year or accident_name is None or stat_name is None or chart_name is None or trend_name is None \
            or scale_name is None:
        return bad_request(request)

    parameters = ((international['regions_title'][lang], list_to_str(regions)),
                  (international['from_title'][lang], from_year),
                  (international['to_title'][lang], to_year),
                  (international['graph_type_title'][lang], chart_name),
                  (international['trend_line_title'][lang], trend_name),
                  (international['reason_title'][lang], accident_name),
                  (international['observed_title'][lang], stat_name),
                  (international['scale_title'][lang], scale_name),)
    return render_to_response('trend_chart_by_url.html', {"type": "trend_chart",
                                                          "title": international['title'][lang],
                                                          "chart_title": international['trend_chart_title'][lang],
                                                          'lang': lang,
                                                          "parameters_title": international['parameters_title'][lang],
                                                          "info_header": international['information_header'][lang],
                                                          "parameters": parameters,
                                                          "url": request.path})


def trend_chart_data(request, lang, regions, from_year, to_year, chart_type, trend_type, accident_type, stat_type,
                     scale_type):
    regions = regions.split(",")
    from_year = int(from_year)
    to_year = int(to_year)
    accident_name = get_accident_name_by_type(accident_type, lang)
    stat_name = get_stat_name_by_type(stat_type, lang)
    chart_name = get_chart_name_by_type(chart_type, lang)
    trend_name = get_trend_name_by_type(trend_type, lang)
    scale_name = get_scale_name_by_type(scale_type, lang)

    if from_year > to_year or accident_name is None or stat_name is None or chart_name is None or trend_name is None \
            or scale_name is None:
        return None

    xAxis = international['year_title'][lang]
    yAxis = stat_name
    chart_title = international['trend_reason_title'][lang]  % (
        stat_name, scale_name, accident_name, from_year, to_year,)
    year_value_type_function = lambda x: x if chart_type == "point" or trend_type != 'no' else str(x)
    data = [[international['year_title'][lang]] + regions] + [[year_value_type_function(year)] for year in range(from_year, to_year + 1)]

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


def pie_chart(request, lang):
    min_year = RegionStat.objects.earliest("year").year
    max_year = RegionStat.objects.latest("year").year
    return render_to_response('pie_chart_with_form.html', {"type": "pie_chart",
                                                           "title": international['title'][lang],
                                                           "chart_title": international['pie_chart_title'][lang],
                                                           'lang': lang,
                                                           "parameters_title": international['parameters_title'][lang],
                                                           "info_header": international['information_header'][lang],
                                                           "regions": get_region_list_for_select(),
                                                           "stat_types": stat_types,
                                                           "from_year": min_year,
                                                           "to_year": max_year})


def pie_chart_url(request, lang, regions, stat_type, from_year, to_year):
    stat_name = get_stat_name_by_type(stat_type, lang)
    parameters = [(international['regions_title'][lang], regions),
                  (international['observed_title'][lang], stat_name),
                  (international['from_title'][lang], from_year),
                  (international['to_title'][lang], to_year)]
    return render_to_response('pie_chart_by_url.html', {"type": "pie_chart",
                                                        "title": international['title'][lang],
                                                        "chart_title": international['pie_chart_title'][lang],
                                                        'lang': lang,
                                                        "parameters_title": international['parameters_title'][lang],
                                                        "info_header": international['information_header'][lang],
                                                        "parameters": parameters,
                                                        "url": request.path})


def pie_chart_data(request, lang, regions, stat_type, from_year, to_year):
    regions = regions.split(",")
    from_year = int(from_year)
    to_year = int(to_year)
    stat_name = get_stat_name_by_type(stat_type, lang)
    chart_title = international['pie_chart_title_param'][lang] % (stat_name, from_year, to_year,)
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

    data = [[international['reason_title'][lang], stat_name]] + [[get_accident_name_by_type(current, lang),
                                                         accident_number[current]] for current in
                                                        accident_number.keys()]
    return HttpResponse(json.dumps({"chart_title": chart_title, "chart_data": data}), content_type="application/json")


def sankey_chart(request, lang):
    min_year = RegionStat.objects.earliest("year").year
    max_year = RegionStat.objects.latest("year").year
    return render_to_response('sankey_chart_with_form.html', {"type": "sankey_chart",
                                                              "title": international['title'][lang],
                                                              "chart_title": international['sankey_chart_title'][lang],
                                                              'lang': lang,
                                                              "parameters_title": international['parameters_title'][lang],
                                                              "info_header": international['information_header'][lang],
                                                              "regions": get_region_list_for_select(),
                                                              "stat_types": stat_types,
                                                              "from_year": min_year,
                                                              "to_year": max_year})


def sankey_chart_url(request, lang, regions, stat_type, from_year, to_year):
    stat_name = get_stat_name_by_type(stat_type, lang)
    parameters = [(international['regions_title'][lang], regions),
                  (international['observed_title'][lang], stat_name),
                  (international['from_title'][lang], from_year),
                  (international['to_title'][lang], to_year)]
    return render_to_response('sankey_chart_by_url.html', {"type": "sankey_chart",
                                                           "title": international['title'][lang],
                                                           "chart_title": international['sankey_chart_title'][lang],
                                                           'lang': lang,
                                                           "parameters_title": international['parameters_title'][lang],
                                                           "info_header": international['information_header'][lang],
                                                           "parameters": parameters,
                                                           "url": request.path})


def sankey_chart_data(request, lang, regions, stat_type, from_year, to_year):
    regions = regions.split(",")
    from_year = int(from_year)
    to_year = int(to_year)
    chart_title = international['sankey_title_param'][lang] % (from_year, to_year,)
    stat_name = get_stat_name_by_type(stat_type, lang)
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
    all_name = get_accident_name_by_type('all', lang)
    driver_name = get_accident_name_by_type('driver', lang)
    broken_name = get_accident_name_by_type('broken', lang)
    roads_name = get_accident_name_by_type('roads', lang)
    pedestrian_name = get_accident_name_by_type('pedestrian', lang)
    driver_and_pedestrian_name = international['driver_pedestrian_title'][lang]
    data = [[international['sankey_chart_from'][lang], international['sankey_chart_to'][lang], stat_name],
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
            [driver_name, get_accident_name_by_type('physical', lang), accident_number['physical']],
            [driver_name, get_accident_name_by_type('juridical', lang), accident_number['juridical']],
            [driver_name, get_accident_name_by_type('hidden', lang), accident_number['hidden']]]

    return HttpResponse(json.dumps({"chart_title": chart_title, "chart_data": data}), content_type="application/json")


def finland_comp(request, lang):
    min_year = RegionStat.objects.earliest("year").year
    max_year = 2012

    return render_to_response('finland_comp_with_form.html', {"type": "finland_comp",
                                                              "title": international['title'][lang],
                                                              "chart_title": international['diff_fin_rus_title'][lang],
                                                              'lang': lang,
                                                              "parameters_title": international['parameters_title'][lang],
                                                              "info_header": international['information_header'][lang],
                                                              "regions": get_region_list_for_select(True),
                                                              "from_year": min_year,
                                                              "to_year": max_year,
                                                              "stat_types": get_finland_types(stat_types),
                                                              "chart_types": chart_types,
                                                              "trend_types": trend_types,
                                                              "scale_types": get_finland_types(scale_types)})


def finland_comp_url(request, lang, regions, from_year, to_year, chart_type, trend_type, stat_type, scale_type):
    regions = regions.split(",")
    from_year = int(from_year)
    to_year = int(to_year)
    accident_name = get_accident_name_by_type('all', lang)
    stat_name = get_stat_name_by_type(stat_type, lang, True)
    chart_name = get_chart_name_by_type(chart_type, lang)
    trend_name = get_trend_name_by_type(trend_type, lang)
    scale_name = get_scale_name_by_type(scale_type, lang, True)

    if from_year > to_year or accident_name is None or stat_name is None or chart_name is None or trend_name is None \
            or scale_name is None:
        return bad_request(request)

    parameters = ((international['regions_title'][lang], list_to_str(regions)),
                  (international['from_title'][lang], from_year),
                  (international['to_title'][lang], to_year),
                  (international['graph_type_title'][lang], chart_name),
                  (international['trend_line_title'][lang], trend_name),
                  (international['reason_title'][lang], accident_name),
                  (international['observed_title'][lang], stat_name),
                  (international['scale_title'][lang], scale_name),)
    return render_to_response('finland_comp_by_url.html', {"type": "finland_comp",
                                                          "title": international['title'][lang],
                                                          "chart_title": international['diff_fin_rus_title'][lang],
                                                          'lang': lang,
                                                          "parameters_title": international['parameters_title'][lang],
                                                          "info_header": international['information_header'][lang],
                                                          "parameters": parameters,
                                                          "url": request.path})


def finland_comp_data(request, lang, regions, from_year, to_year, chart_type, trend_type, stat_type, scale_type):
    regions = regions.split(",")
    from_year = int(from_year)
    to_year = int(to_year)
    accident_name = get_accident_name_by_type('all', lang)
    stat_name = get_stat_name_by_type(stat_type, lang, True)
    chart_name = get_chart_name_by_type(chart_type, lang)
    trend_name = get_trend_name_by_type(trend_type, lang)
    scale_name = get_scale_name_by_type(scale_type, lang, True)

    if from_year > to_year or accident_name is None or stat_name is None or chart_name is None or trend_name is None \
            or scale_name is None:
        return None

    xAxis = international['year_title'][lang]
    yAxis = stat_name
    chart_title = international['diff_fin_param_title'][lang] % (stat_name, scale_name, from_year, to_year,)
    year_value_type_function = lambda x: x if chart_type == "point" or trend_type != 'no' else str(x)
    data = [[international['year_title'][lang]] + regions] + [[year_value_type_function(year)] for year in range(from_year, to_year + 1)]

    stat_data = RegionStat.objects.filter(accident_type='all')
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
                    region_stat_data.filter(year=from_year + i)[0].get_stat_number(stat_type) / scale_function(
                        region, from_year + i))
            except ArithmeticError:
                data[i + 1].append(0)
    return HttpResponse(json.dumps({"chart_title": chart_title,
                                    "xAxis_title": xAxis,
                                    "yAxis_title": yAxis,
                                    "chart_data": data,
                                    "chart_type": chart_type,
                                    "trend_type": trend_type}), content_type="application/json")
