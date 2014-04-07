# -*- coding: utf-8 -*-
__author__ = 'viosng'


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

stat_types = (
    ('hurt', u'Число пострадавших'),
    ('dead', u'Число умерших'),
    ('injured', u'Число раненых'),
    ('accident', u'Число ДТП'),
)

scale_types = (
    ('no', u'без масштаба'),
    ('population', u'на 100 тыс. жителей'),
    ('transport', u'на 10 тыс. транспортных средств'),
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


def get_name(searched_type, types):
    for cur in types:
        if cur[0] == searched_type:
            return cur[1]
    return None


def get_accident_name_by_type(searched_accident_type):
    return get_name(searched_accident_type, accident_types)


def get_chart_name_by_type(searched_chart_type):
    return get_name(searched_chart_type, chart_types)


def get_stat_name_by_type(searched_stat_type):
    return get_name(searched_stat_type, stat_types)


def get_trend_name_by_type(searched_trend_type):
    return get_name(searched_trend_type, trend_types)


def get_scale_name_by_type(searched_scale_type):
    return get_name(searched_scale_type, scale_types)