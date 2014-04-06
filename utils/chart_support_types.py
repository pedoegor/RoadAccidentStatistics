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

hurt_types = (
    ('hurt', u'Число пострадавших'),
    ('dead', u'Число умерших'),
    ('injured', u'Число раненых'),
    ('accident', u'Число ДТП'),
    ('transport', u'Число единиц транспортных средств'),
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

def get_accident_name_by_type(searched_accident_type):
    for accident_type in accident_types:
        if accident_type[0] == searched_accident_type:
            return accident_type[1]
    return None


def get_chart_name_by_type(searched_chart_type):
    for chart_type in chart_types:
        if chart_type[0] == searched_chart_type:
            return chart_type[1]
    return None


def get_hurt_name_by_type(searched_hurt_type):
    for hurt_type in hurt_types:
        if hurt_type[0] == searched_hurt_type:
            return hurt_type[1]
    return None


def get_trend_name_by_type(searched_trend_type):
    for trend_type in trend_types:
        if trend_type[0] == searched_trend_type:
            return trend_type[1]
    return None