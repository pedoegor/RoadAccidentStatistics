from django.db import models


class StatSubject(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    deadNumber = models.IntegerField()
    injuredNumber = models.IntegerField()
    parent = models.ForeignKey("self", null=True, default=None)

    def __unicode__(self):
        parent_name = "None" if self.parent is None else self.parent.name
        return u'Subject: %s, dead: %s, injured: %s, year: %s, parent: %s' % (self.name, self.deadNumber,
                                                                              self.injuredNumber, self.year,
                                                                              parent_name)