# -*- coding: utf-8 -*-
from django.db import models
from utils.chart_support_types import *


class Region(models.Model):
    name = models.CharField(max_length=100, unique=True)
    parent = models.ForeignKey("self", null=True, default=None)

    def __unicode__(self):
        return u'%s' % (self.name,)


class RegionStat(models.Model):
    region = models.ForeignKey(Region)
    year = models.IntegerField()
    accident_type = models.CharField(max_length=10, choices=accident_types_models)
    dead_number = models.IntegerField()
    injured_number = models.IntegerField()
    accident_number = models.IntegerField()

    class Meta:
        unique_together = ('region', 'year', 'accident_type',)

    def get_stat_number(self, hurt_type):
        if hurt_type == 'injured':
            return self.injured_number
        if hurt_type == 'dead':
            return self.dead_number
        if hurt_type == 'hurt':
            return self.dead_number + self.injured_number
        return self.accident_number

    def __unicode__(self):
        return u'RegionStat: %s, accident_type: %s, dead: %s, injured: %s, accident number: %s, year: %s' % (
            self.region.name,
            self.accident_type,
            self.dead_number,
            self.injured_number,
            self.accident_number,
            self.year)


class RegionCrashedTransport(models.Model):
    region = models.ForeignKey(Region)
    year = models.IntegerField()
    crashed_transport_number = models.BigIntegerField()

    class Meta:
        unique_together = ('region', 'year',)

    def __unicode__(self):
        return u'RegionPopulation: %s, crashed transport number: %s, year: %s' % (self.region.name,
                                                                                  self.crashed_transport_number,
                                                                                  self.year)


class RegionPopulation(models.Model):
    region = models.ForeignKey(Region)
    year = models.IntegerField()
    population = models.BigIntegerField()

    class Meta:
        unique_together = ('region', 'year',)

    def __unicode__(self):
        return u'RegionPopulation: %s, population: %s, year: %s' % (self.region.name, self.population, self.year)
