# -*- coding: utf-8 -*-
import xlrd
from RoadAccidentStatistics.models import Region
from RoadAccidentStatistics.models import RegionStat
from RoadAccidentStatistics.models import RegionPopulation
from RoadAccidentStatistics.models import RegionCrashedTransport
from RoadAccidentStatistics.views import get_region_by_name
from RoadAccidentStatistics.views import *
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

regions_structure = (
    (u'Российская Федерация', None),
    (u'Центральный округ', u'Российская Федерация'),
    (u'Северо-Западный округ', u'Российская Федерация'),
    (u'Южный округ', u'Российская Федерация'),
    (u'Приволжский округ', u'Российская Федерация'),
    (u'Уральский округ', u'Российская Федерация'),
    (u'Сибирский округ', u'Российская Федерация'),
    (u'Дальневосточный округ', u'Российская Федерация'),
    (u'Белгородская область', u'Центральный округ'),
    (u'Брянская область', u'Центральный округ'),
    (u'Владимирская область', u'Центральный округ'),
    (u'Воронежская область', u'Центральный округ'),
    (u'Ивановская область', u'Центральный округ'),
    (u'Калужская область', u'Центральный округ'),
    (u'Костромская область', u'Центральный округ'),
    (u'Курская область', u'Центральный округ'),
    (u'Липецкая область', u'Центральный округ'),
    (u'г. Москва', u'Центральный округ'),
    (u'Московская область', u'Центральный округ'),
    (u'Орловская область', u'Центральный округ'),
    (u'Рязанская область', u'Центральный округ'),
    (u'Смоленская область', u'Центральный округ'),
    (u'Тамбовская область', u'Центральный округ'),
    (u'Тверская область', u'Центральный округ'),
    (u'Тульская область', u'Центральный округ'),
    (u'Ярославская область', u'Центральный округ'),
    (u'Республика Карелия', u'Северо-Западный округ'),
    (u'Республика Коми', u'Северо-Западный округ'),
    (u'Архангельская область', u'Северо-Западный округ'),
    (u'Вологодская область', u'Северо-Западный округ'),
    (u'Калининградская область', u'Северо-Западный округ'),
    (u'Ленинград. обл. и г. С.-Петербург', u'Северо-Западный округ'),
    (u'Ленинградская область', u'Северо-Западный округ'),
    (u'г. С.-Петербург', u'Северо-Западный округ'),
    (u'Мурманская область', u'Северо-Западный округ'),
    (u'Новгородская область', u'Северо-Западный округ'),
    (u'Псковская область', u'Северо-Западный округ'),
    (u'Ненецкий авт.округ', u'Северо-Западный округ'),
    (u'Республика Адыгея', u'Южный округ'),
    (u'Республика Дагестан', u'Южный округ'),
    (u'Республика Ингушетия', u'Южный округ'),
    (u'Кабардино-Балкарская Республика', u'Южный округ'),
    (u'Республика Калмыкия', u'Южный округ'),
    (u'Карачаево-Черкесская Республика', u'Южный округ'),
    (u'Республика Северная Осетия', u'Южный округ'),
    (u'Чеченская Республика', u'Южный округ'),
    (u'Краснодарский край', u'Южный округ'),
    (u'Ставропольский край', u'Южный округ'),
    (u'Астраханская область', u'Южный округ'),
    (u'Волгоградская область', u'Южный округ'),
    (u'Ростовская область', u'Южный округ'),
    (u'Республика Башкортостан', u'Приволжский округ'),
    (u'Республика Марий Эл', u'Приволжский округ'),
    (u'Республика Мордовия', u'Приволжский округ'),
    (u'Республика Татарстан', u'Приволжский округ'),
    (u'Удмуртская Республика', u'Приволжский округ'),
    (u'Чувашская Республика', u'Приволжский округ'),
    (u'Пермский край', u'Приволжский округ'),
    (u'Кировская область', u'Приволжский округ'),
    (u'Нижегородская область', u'Приволжский округ'),
    (u'Оренбургская область', u'Приволжский округ'),
    (u'Пензенская область', u'Приволжский округ'),
    (u'Самарская область', u'Приволжский округ'),
    (u'Саратовская область', u'Приволжский округ'),
    (u'Ульяновская область', u'Приволжский округ'),
    (u'Курганская область', u'Уральский округ'),
    (u'Свердловская область', u'Уральский округ'),
    (u'Тюменская область', u'Уральский округ'),
    (u'Челябинская область', u'Уральский округ'),
    (u'Ханты-мансийский авт.округ', u'Уральский округ'),
    (u'Ямало-ненецкий авт.округ', u'Уральский округ'),
    (u'Республика Алтай', u'Сибирский округ'),
    (u'Республика Бурятия', u'Сибирский округ'),
    (u'Республика Тыва', u'Сибирский округ'),
    (u'Республика Хакасия', u'Сибирский округ'),
    (u'Алтайский край', u'Сибирский округ'),
    (u'Красноярский край', u'Сибирский округ'),
    (u'Иркутская область', u'Сибирский округ'),
    (u'Кемеровская область', u'Сибирский округ'),
    (u'Новосибирская область', u'Сибирский округ'),
    (u'Омская область', u'Сибирский округ'),
    (u'Томская область', u'Сибирский округ'),
    (u'Читинская область', u'Сибирский округ'),
    (u'Агинский бурятский авт.округ', u'Сибирский округ'),
    (u'Таймырский авт.округ', u'Сибирский круг'),
    (u'Усть-ордынский Бурятский авт.окр.', u'Сибирский округ'),
    (u'Эвенкийский авт.округ', u'Сибирский округ'),
    (u'Республика Саха (Якутия)', u'Дальневосточный округ'),
    (u'Приморский край', u'Дальневосточный округ'),
    (u'Хабаровский край', u'Дальневосточный округ'),
    (u'Амурская область', u'Дальневосточный округ'),
    (u'Камчатская область', u'Дальневосточный округ'),
    (u'Магаданская область', u'Дальневосточный округ'),
    (u'Сахалинская область', u'Дальневосточный округ'),
    (u'Корякский авт. округ', u'Дальневосточный округ'),
    (u'Еврейская автономная область', u'Дальневосточный округ'),
    (u'Чукотский авт.округ', u'Дальневосточный округ')
)


def my_int(string):
    if string == '':
        return 0
    else:
        return int(string)

reasons = ['all', '', 'driver', 'drunk', 'juridical', 'physical', 'pedestrian', 'children', 'broken',
            'roads', 'hidden', 'hard']


def make_stat_subj(sheet, rowx, year, sheet_number):
    shift = 0 if sheet_number % 11 == 0 else 1
    subj = RegionStat()
    name = str(sheet.cell_value(rowx, 0)).replace('*', '')
    name = name.strip()

    if len(name) < 5:
        return
    subj.region = get_region_by_name(name)
    subj.year = year
    subj.accident_type = reasons[sheet_number]
    subj.dead_number = my_int(sheet.cell_value(rowx, 3 + shift))
    subj.injured_number = my_int(sheet.cell_value(rowx, 5 + shift))
    subj.accident_number = my_int(sheet.cell_value(rowx, 1))
    subj.save()
    return name


def make_population_stat(sheet, rowx, year):
    subj = RegionPopulation()
    name = str(sheet.cell_value(rowx, 0)).replace('*', '')
    name = name.strip()
    if len(name) < 5:
        return
    subj.region = get_region_by_name(name)
    subj.year = year
    subj.population = my_int(sheet.cell_value(rowx, 4))
    subj.save()
    return name


def make_transport_stat(sheet, rowx, year):
    subj = RegionCrashedTransport()
    name = str(sheet.cell_value(rowx, 0)).replace('*', '')
    name = name.strip()
    if len(name) < 5:
        return
    subj.region = get_region_by_name(name)
    subj.year = year
    subj.crashed_transport_number = my_int(sheet.cell_value(rowx, 3))
    subj.save()
    return name


def regions_info(request, sheet_number=-1):
    y = ''
    for year in range(2004, 2013):
        file_name = "tables/" + str(year) + ".xls"
        y = y + ", " + str(year)
        if sheet_number == 1:
            regions_relativity_info(file_name, year)

        if sheet_number >= 0:
            regions_info_from_sheet(file_name, year, sheet_number)
        else:
            regions_info_from_sheet(file_name, year, 0)
            regions_relativity_info(file_name, year)
            for sh in range(2, len(reasons)):
                regions_info_from_sheet(file_name, year, sh)
    return HttpResponse("add years: " + y)


def regions_info_from_sheet(file_name, year, sheet_number):
    book = xlrd.open_workbook(file_name, formatting_info=True)
    sh = book.sheet_by_index(sheet_number)
    for rx in range(4, sh.nrows):
        if make_stat_subj(sh, rx, year, sheet_number) == "Дальневосточный округ":
            break


def regions_relativity_info(file_name, year):
    book = xlrd.open_workbook(file_name, formatting_info=True)
    sh = book.sheet_by_index(1)
    for rx in range(4, sh.nrows - 2):
        if make_population_stat(sh, rx, year) == "Дальневосточный округ":
            break
        make_transport_stat(sh, rx, year)

