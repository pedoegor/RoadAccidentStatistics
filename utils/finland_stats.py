# -*- coding: utf-8 -*-
__author__ = 'viosng'
from RoadAccidentStatistics.views import *


def add_stats():
    region = Region(name=u'Финляндия', parent=None)
    region.save()
    data = [[2004,  375,    8791],
            [2005,	379,	8983],
            [2006,	336,	8580],
            [2007,	380,	8446],
            [2008,	344,	8513],
            [2009,	279,	8057],
            [2010,	272,	7673],
            [2011,	292,	7931],
            [2012,	255,	7088]]
    for d in data:
        RegionStat.objects.create(region=region, year=d[0], accident_type='all', dead_number=d[1], injured_number=d[2], accident_number=0)

    population = [[2004,	5228000],
                    [2005,	5246000],
                    [2006,	5266000],
                    [2007,	5289000],
                    [2008,	5313000],
                    [2009,	5339000],
                    [2010,	5375000],
                    [2011,	5403000],
                    [2012,	5426000],
                    [2013,	5450000]]

    for d in population:
        RegionPopulation.objects.create(region=region, year=d[0], population=d[1])