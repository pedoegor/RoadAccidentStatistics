# -*- coding: utf-8 -*-
from django.db import models


class Region(models.Model):
    name = models.CharField(max_length=100)
    english_name = models.CharField(max_length=100, blank=True)
    parent = models.ForeignKey("self", null=True, default=None)

    def __unicode__(self):
        parent_name = "None" if self.parent is None else self.parent.name
        return u'Region: %s, parent: %s' % (self.name, parent_name)


class RegionStat(models.Model):
    accident_types = (
        ('driver', u'Нарушение ПДД водителями транспортных средств'),
        ('drunk', u'Нарушение ПДД водителями транспортных средств в состоянии алкогольного опьянения'),
        ('juridical', u'Нарушение ПДД водителями транспортных средств юридических лиц'),
        ('physical', u'Нарушение ПДД водителями транспортных средств физических лиц'),
        ('pedestrian', u'Нарушение ПДД пешеходами'),
        ('children', u'ДТП с участием детей'),
        ('broken', u'ДТП из-за эксплуатации технически неисправных транспортных средств'),
        ('roads', u'ДТП из-за неудовлетворительного состояния улиц и дорог'),
        ('hidden', u'ДТП с участием неустановленных транспортных средств'),
        ('all', u'Общее количество ДТП'),
    )
    region = models.ForeignKey(Region)
    year = models.IntegerField()
    accident_type = models.CharField(max_length=10, choices=accident_types)
    deadNumber = models.IntegerField()
    injuredNumber = models.IntegerField()

    def get_hurted_number(self):
        return self.deadNumber + self.injuredNumber

    def __unicode__(self):
        return u'RegionStat: %s, accident_type: %s, dead: %s, injured: %s, year: %s' % (self.region.name,
                                                                                        self.accident_type,
                                                                                        self.deadNumber,
                                                                                        self.injuredNumber,
                                                                                        self.year)


class RegionCrashedTransport(models.Model):
    region = models.ForeignKey(Region)
    year = models.IntegerField()
    crashed_transport_number = models.BigIntegerField()

    def __unicode__(self):
        return u'RegionPopulation: %s, crashed transport number: %s, year: %s' % (self.region.name,
                                                                                  self.crashed_transport_number,
                                                                                  self.year)


class RegionPopulation(models.Model):
    region = models.ForeignKey(Region)
    year = models.IntegerField()
    population = models.BigIntegerField()

    def __unicode__(self):
        return u'RegionPopulation: %s, population: %s, year: %s' % (self.region.name, self.population, self.year)


