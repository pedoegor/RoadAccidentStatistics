from django.db import models


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
    deadNumber = models.IntegerField()
    injuredNumber = models.IntegerField()

    def __unicode__(self):
        return u'RegionStat: %s, dead: %s, injured: %s, year: %s' % (self.region.name, self.deadNumber,
                                                                              self.injuredNumber, self.year)


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


