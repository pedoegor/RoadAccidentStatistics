# -*- coding: utf-8 -*-
from django.db import models
from utils.chart_support_types import *

class Region(models.Model):
    name = models.CharField(max_length=100)
    english_name = models.CharField(max_length=100, blank=True)
    parent = models.ForeignKey("self", null=True, default=None)

    def __unicode__(self):
        parent_name = "None" if self.parent is None else self.parent.name
        return u'Region: %s, parent: %s' % (self.name, parent_name)


class RegionStat(models.Model):

    region = models.ForeignKey(Region)
    year = models.IntegerField()
    accident_type = models.CharField(max_length=10, choices=accident_types)
    dead_number = models.IntegerField()
    injured_number = models.IntegerField()
    accident_number = models.IntegerField()

    def get_stat_number(self, hurt_type):
        if hurt_type == 'injured':
            return self.injured_number
        if hurt_type == 'dead':
            return self.dead_number
        if hurt_type == 'hurt':
            return self.dead_number + self.injured_number
        return self.accident_number

    def __unicode__(self):
        return u'RegionStat: %s, accident_type: %s, dead: %s, injured: %s, accident number: %s, year: %s' % (self.region.name,
                                                                                        self.accident_type,
                                                                                        self.dead_number,
                                                                                        self.injured_number,
                                                                                        self.accident_number,
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


class DownloadFile(models.Model):
    name = models.CharField(max_length=200)
