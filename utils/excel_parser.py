#Скрипт парсит xls заданного формата и возвращает список объектов типа StatSubject 
#   основная функция regions_info принимает на вход адрес, где лежит желаемая xls, год и
#   номер страницы, который мы хотим распарсить. По умолчанию парсит все, кроме 
#   московских страничек. Возвращает ышеописанный список
#
#WARNING! Проверить, что "таблица 2", в которой не нужная нам информация, расположена на 2ом листе xls, иначе парсер сломается 
#

import xlrd
from RoadAccidentStatistics.models import StatSubject
# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


#class StatSubject():
#    name = ""
#    year = 0
#    deadNumber = 0
#    injuredNumber = 0
#    sheet_type = ''
#    reasone = ''
#
#    def __unicode__(self):
#        return u'Subject: %s, dead: %s, injured: %s, year: %s, reasone: %s' % (self.name, self.deadNumber, self.injuredNumber, self.year, self.reasone)

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
    subj.reasone = reasons[sheet_number]
    subj.deadNumber = my_int(sheet.cell_value(rowx, 3 + shift))
    subj.injuredNumber = my_int(sheet.cell_value(rowx, 5 + shift))
    subj.sheet_type = reasons[sheet_number]
    return subj


def regions_info(file_name, year, sheet_number=-1):
    if sheet_number > 0:
        return regions_info_from_sheet(file_name, year, sheet_number)
    else:
        r = []
        for sh in range(0, len(reasons)):
            if sh == 1:
                continue
            r = r + regions_info_from_sheet(file_name, year, sh)
        return r


def regions_info_from_sheet(file_name, year, sheet_number):
    book = xlrd.open_workbook(file_name, formatting_info=True)
    sh = book.sheet_by_index(sheet_number)
    regions = []
    for rx in range(4, sh.nrows - 2):
        reg = make_stat_subj(sh, rx, year, sheet_number)

        if reg.name[:1] == "*":
            continue

        regions.append(reg)

    return regions

#r = regions_info("../tables/2012.xls", 2012)
#for i in r:
#    print i.__unicode__()    

