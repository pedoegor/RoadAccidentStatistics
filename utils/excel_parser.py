import xlrd
from RoadAccidentStatistics.models import StatSubject
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def make_stat_subj(sheet, rowx, _year):
    subj = StatSubject()
    subj.name = str(sheet.cell_value(rowx, 0));
    subj.year = _year
    subj.deadNumber = int(sheet.cell_value(rowx, 3));
    subj.injuredNumber = int(sheet.cell_value(rowx, 5));
    return subj


def regions_info(file_name, year):
    book = xlrd.open_workbook(file_name, formatting_info=True)
    #TODO make flexible choose of sheet
    sh = book.sheet_by_index(0)
    regions = []
    last_parent = 0
    for rx in range(4, sh.nrows-2):
        reg = make_stat_subj(sh, rx, year)
        
        if reg.name[:1] == "*":
            continue 
            
        regions.append(reg)
        if reg.name[:5] != 5*" " and reg.name[:1] == " ":
            print reg.name
            for i in range(last_parent + 1, len(regions)-1):
                regions[i].parent = reg
            reg._parent = regions[0]
            last_parent = len(regions)-1
            
    regions[0].parent = regions[0]
     
    for region in regions[1:]:
       print region.name, region.parent.name

regions_info("../tables/2012.xls", 2012)
