# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from RoadAccidentStatistics.models import Region
from utils.region_offset import RegionOffset


def render_object_hierarchy(request):
    def dfs(region, level, region_list):
        region_list.append(RegionOffset(region.name, level))
        for child in region.region_set.all():
            dfs(child, level + 1, region_list)

    regions = []
    dfs(Region.objects.filter(parent=None)[0], 0, regions)
    return render_to_response('hierarchy.template.html', {'regions': regions})


def dashboard(request):
    return render_to_response('dashboard.html', {'title': u'Статистика ДТП'})
