# -*- coding: utf-8 -*-
__author__ = 'viosng'


#(type, russian_name, finland_comparison),

accident_types = (
    ('driver', u'Нарушение ПДД водителями ТС',),
    ('drunk', u'Нарушение ПДД водителями ТС в состоянии алкогольного опьянения',),
    ('juridical', u'Нарушение ПДД водителями ТС юридических лиц',),
    ('physical', u'Нарушение ПДД водителями ТС физических лиц',),
    ('pedestrian', u'Нарушение ПДД пешеходами',),
    ('children', u'ДТП с участием детей',),
    ('broken', u'ДТП из-за эксплуатации технически неисправных ТС',),
    ('roads', u'ДТП из-за неудовлетворительного состояния улиц и дорог',),
    ('hidden', u'ДТП с участием неустановленных транспортных средств',),
    ('all', u'Общее количество ДТП'),
)

stat_types = (
    ('hurt', u'Число пострадавших', True),
    ('dead', u'Число умерших', True),
    ('injured', u'Число раненых', True),
    ('accident', u'Число ДТП', False),
)

scale_types = (
    ('no', u'без масштаба', True),
    ('population', u'на 100 тыс. жителей', True),
    ('transport', u'на 10 тыс. транспортных средств', False),
)

chart_types = (
    ('column', u'Вертикальная гистограмма'),
    ('bar', u'Горизонтальная гистограмма'),
    ('area', u'Диаграмма с областями'),
    ('line', u'Линейный график'),
    ('point', u'Точечный график'),
)

trend_types = (
    ('no', u'Нет'),
    ('linear', u'Линейная'),
    ('exponential', u'Экспоненциальная'),
)


def get_name(searched_type, types, only_finland_comp=False):
    for cur in types:
        if cur[0] == searched_type:
            if only_finland_comp and not cur[2]:
                return None
            return cur[1]
    return None


def get_accident_name_by_type(searched_accident_type, only_finland_comp=False):
    return get_name(searched_accident_type, accident_types, only_finland_comp)


def get_chart_name_by_type(searched_chart_type, only_finland_comp=False):
    return get_name(searched_chart_type, chart_types, only_finland_comp)


def get_stat_name_by_type(searched_stat_type, only_finland_comp=False):
    return get_name(searched_stat_type, stat_types, only_finland_comp)


def get_trend_name_by_type(searched_trend_type):
    return get_name(searched_trend_type, trend_types)


def get_scale_name_by_type(searched_scale_type, only_finland_comp=False):
    return get_name(searched_scale_type, scale_types, only_finland_comp)

def get_finland_types(types):
    new_types = []
    for t in types:
        if t[2]:
            new_types.append(t)
    return new_types