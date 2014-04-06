# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from RoadAccidentStatistics.models import *
from utils.wrap_classes import *
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
    parameters = [Parameter(u'Регионы', regions), Parameter(u'С', from_year), Parameter(u'По', to_year)]
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


def pie_chart(request):
    min_year = RegionStat.objects.earliest("year").year
    max_year = RegionStat.objects.latest("year").year
    return render_to_response('pie_chart_with_form.html', {"type": "pie_chart",
                                                           "title": u'Статистика ДТП',
                                                           "chart_title": u'Круговая диаграмма причин ДТП',
                                                           "parameters_title": u'Параметры',
                                                           "info_header": u'Информация',
                                                           "regions": get_region_list_for_select(),
                                                           "years": [x for x in range(min_year, max_year + 1)]})


def pie_chart_url(request, regions, from_year, to_year):
    parameters = [Parameter(u'Регионы', regions), Parameter(u'С', from_year), Parameter(u'По', to_year)]
    return render_to_response('pie_chart_by_url.html', {"type": "pie_chart",
                                                        "title": u'Статистика ДТП',
                                                        "chart_title": u'Круговая диаграмма причин ДТП',
                                                        "parameters_title": u'Параметры',
                                                        "info_header": u'Информация',
                                                        "parameters": parameters,
                                                        "url": request.path})


def pie_chart_data(request, regions, from_year, to_year):
    regions = regions.split(",")
    from_year = int(from_year)
    to_year = int(to_year)

    chart_title = u'Причины ДТП с %s по %s года' % (from_year, to_year,)

    accident_number = {
        #'driver': 0,
        #'drunk': 0,
        'juridical': 0,
        'physical': 0,
        'pedestrian': 0,
        #'children': 0,
        'broken': 0,
        'roads': 0,
        'hidden': 0,
        #u'all': 0,
    }

    driverAccidentName = u'Нарушение ПДД водителями транспортных средств'
    drunkAccidentName = u'Нарушение ПДД водителями транспортных средств в состоянии алкогольного опьянения'
    juridicalAccidentName = u'Нарушение ПДД водителями транспортных средств юридических лиц'
    physicalAccidentName = u'Нарушение ПДД водителями транспортных средств физических лиц'
    pedestrianAccidentName = u'Нарушение ПДД пешеходами'
    childrenAccidentName = u'ДТП с участием детей'
    brokenAccidentName = u'ДТП из-за эксплуатации технически неисправных транспортных средств'
    roadsAccidentName = u'ДТП из-за неудовлетворительного состояния улиц и дорог'
    hiddenAccidentName = u'ДТП с участием неустановленных транспортных средств'
    #allAccidentName = u'Общее количество ДТП'

    driverAccidentNumber = 0
    drunkAccidentNumber = 0
    juridicalAccidentNumber = 0
    physicalAccidentNumber = 0
    pedestrianAccidentNumber = 0
    childrenAccidentNumber = 0
    brokenAccidentNumber = 0
    roadsAccidentNumber = 0
    hiddenAccidentNumber = 0
    #allAccidentNumber = 0

    for region_name in regions:
        region = get_region_by_name(region_name)
        for year in range(from_year, to_year + 1):
            stat_objects = RegionStat.objects.filter(region=region, year=year)
            for current in stat_objects:
                if str(current.accident_type) not in ['all', 'driver', 'drunk', 'children']:
                    accident_number[str(current.accident_type)] += current.get_hurted_number()

    data = [['Accident type', 'Accident number']]
    for current in accident_number.keys():
        data.append([current, accident_number[current]])

    return HttpResponse(json.dumps({"chart_title": chart_title, "chart_data": data}), content_type="application/json")


def sankey_chart(request):
    min_year = RegionStat.objects.earliest("year").year
    max_year = RegionStat.objects.latest("year").year
    return render_to_response('sankey_chart_with_form.html', {"type": "sankey_chart",
                                                              "title": u'Статистика ДТП',
                                                              "chart_title": u'Потоковая диаграмма причин ДТП',
                                                              "parameters_title": u'Параметры',
                                                              "info_header": u'Информация',
                                                              "regions": get_region_list_for_select(),
                                                              "years": [x for x in range(min_year, max_year + 1)]})


def sankey_chart_url(request, regions, from_year, to_year):
    parameters = [Parameter(u'Регионы', regions), Parameter(u'С', from_year), Parameter(u'По', to_year)]
    return render_to_response('sankey_chart_by_url.html', {"type": "sankey_chart",
                                                           "title": u'Статистика ДТП',
                                                           "chart_title": u'Потоковая диаграмма причин ДТП',
                                                           "parameters_title": u'Параметры',
                                                           "info_header": u'Информация',
                                                           "parameters": parameters,
                                                           "url": request.path})


def sankey_chart_data(request, regions, from_year, to_year):
    regions = regions.split(",")
    from_year = int(from_year)
    to_year = int(to_year)

    chart_title = u'Причины и виновники ДТП с %s по %s года' % (from_year, to_year,)

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

    driverAccidentName = u'Нарушение ПДД водителями транспортных средств'
    drunkAccidentName = u'Нарушение ПДД водителями транспортных средств в состоянии алкогольного опьянения'
    juridicalAccidentName = u'Нарушение ПДД водителями транспортных средств юридических лиц'
    physicalAccidentName = u'Нарушение ПДД водителями транспортных средств физических лиц'
    pedestrianAccidentName = u'Нарушение ПДД пешеходами'
    childrenAccidentName = u'ДТП с участием детей'
    brokenAccidentName = u'ДТП из-за эксплуатации технически неисправных транспортных средств'
    roadsAccidentName = u'ДТП из-за неудовлетворительного состояния улиц и дорог'
    hiddenAccidentName = u'ДТП с участием неустановленных транспортных средств'
    allAccidentName = u'Общее количество ДТП'

    driverAccidentNumber = 0
    drunkAccidentNumber = 0
    juridicalAccidentNumber = 0
    physicalAccidentNumber = 0
    pedestrianAccidentNumber = 0
    childrenAccidentNumber = 0
    brokenAccidentNumber = 0
    roadsAccidentNumber = 0
    hiddenAccidentNumber = 0
    allAccidentNumber = 0

    for region_name in regions:
        region = get_region_by_name(region_name)
        for year in range(from_year, to_year + 1):
            stat_objects = RegionStat.objects.filter(region=region, year=year)
            for current in stat_objects:
                accident_number[str(current.accident_type)] += current.get_hurted_number()

    data = []


    data.append(['all', 'roads', accident_number['roads']])
    data.append(['all', 'broken', accident_number['broken']])

    data.append(['all', 'driver or pedestrian', accident_number['driver'] + accident_number['pedestrian']])



    data.append(['driver or pedestrian', 'driver', accident_number['driver']])


    data.append(['driver', 'physical', accident_number['physical']])
    data.append(['driver', 'juridical', accident_number['juridical']])
    data.append(['driver', 'hidden', accident_number['hidden']])

    data.append(['driver or pedestrian', 'pedestrian', accident_number['pedestrian']])



    return HttpResponse(json.dumps({"chart_title": chart_title, "chart_data": data}), content_type="application/json")



