# -*- coding: utf-8 -*-
import xlrd
#from RoadAccidentStatistics.models import StatSubject

import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class StatSubject():
    name = ""
    year = 0
    deadNumber = 0
    injuredNumber = 0
    sheet_type = ''
    reason = ''

    def __unicode__(self):
        return u'Subject: %s, dead: %s, injured: %s, year: %s, reason: %s' % (self.name, self.deadNumber,
                                                                              self.injuredNumber, self.year,
                                                                              self.reason)


class RelativityStat:
    name = ""
    year = 0
    dtpNumber = 0
    injuredNumber = 0

    def __unicode__(self):
        return u'Subject: %s, dtp: %s, injured: %s, year: %s' % (self.name, self.dtpNumber,
                                                                 self.injuredNumber, self.year)


def my_int(string):
    if string == '':
        return None
    else:
        return int(string)


reasons = ['general', '', 'driver', 'drunk', 'legal_car', 'individual', 'foot', 'children', 'technical',
           'bed_roads', 'escape', 'heavy']


def make_stat_subj(sheet, rowx, year, sheet_number):
    shift = 0 if sheet_number % 11 == 0 else 1
    subj = StatSubject()
    subj.name = str(sheet.cell_value(rowx, 0))
    subj.year = year
    subj.reason = reasons[sheet_number]
    subj.deadNumber = my_int(sheet.cell_value(rowx, 3 + shift))
    subj.injuredNumber = my_int(sheet.cell_value(rowx, 5 + shift))
    subj.sheet_type = reasons[sheet_number]
    return subj


def make_relativity_stat(sheet, rowx, year):
    shift = 4   # because columns B..E are hidden
    subj = RelativityStat()
    subj.name = str(sheet.cell_value(rowx, 0))
    subj.year = year
    subj.dtpNumber = my_int(sheet.cell_value(rowx, 1 + shift))
    subj.injuredNumber = my_int(sheet.cell_value(rowx, 3 + shift))
    return subj


def regions_info(file_name, year, sheet_number=-1):
    if sheet_number == 1:
        return regions_relativity_info(file_name, year)

    if sheet_number >= 0:
        return regions_info_from_sheet(file_name, year, sheet_number)
    else:
        r = []
        for sh in range(0, len(reasons)):
            if sh == 1:
                r = r + regions_relativity_info(file_name, year)
            else:
                r = r + regions_info_from_sheet(file_name, year, sh)
        return r


def regions_info_from_sheet(file_name, year, sheet_number):
    book = xlrd.open_workbook(file_name, formatting_info=True)
    sh = book.sheet_by_index(sheet_number)
    regions = []
    for rx in range(4, sh.nrows - 2):
        reg = make_stat_subj(sh, rx, year, sheet_number)
        if reg.name[:1] != "*" and reg.name[1:] != "1":
            regions.append(reg)
    return regions


def regions_relativity_info(file_name, year):
    book = xlrd.open_workbook(file_name, formatting_info=True)
    sh = book.sheet_by_index(1)
    print sh.cell_value(0, 0)
    regions = []
    for rx in range(4, sh.nrows - 2):
        reg = make_relativity_stat(sh, rx, year)
        if reg.name[:1] != "*" and reg.name[1:] != "1":
            regions.append(reg)
    return regions

r = regions_info("../tables/2012.xls", 2012, 1)
for i in r:
    print i.__unicode__()

