from django.shortcuts import render_to_response
from utils.region_offset import RegionOffset


def render_object_hierarchy(request):
    regions = [RegionOffset("Region1", 0), RegionOffset("Region2", 1)]
    return render_to_response('hierarchy.template.html', {'regions': regions})



