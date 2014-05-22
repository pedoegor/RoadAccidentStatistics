# -*- coding: utf-8 -*-
__author__ = 'viosng'


#contains sorted list of tables that contains tables with reason
reason_table_numbers = [0, 2, 3, 4, 5, 6, 8, 9, 10]


#keys - tables number, values - accident types
reasons = {
    0: 'all',
    2: 'driver',
    3: 'drunk',
    4: 'juridical',
    5: 'physical',
    6: 'pedestrian',
    7: 'children',
    8: 'broken',
    9: 'roads',
    10: 'hidden',
}


accident_types_models = (
    ('driver', u'Нарушение ПДД водителями ТС',),
    ('drunk', u'Нарушение ПДД водителями ТС в состоянии алкогольного опьянения',),
    ('juridical', u'Нарушение ПДД водителями ТС юридических лиц',),
    ('physical', u'Нарушение ПДД водителями ТС физических лиц',),
    ('pedestrian', u'Нарушение ПДД пешеходами',),
    ('broken', u'ДТП из-за эксплуатации технически неисправных ТС',),
    ('roads', u'ДТП из-за неудовлетворительного состояния улиц и дорог',),
    ('hidden', u'ДТП с участием неустановленных транспортных средств',),
    ('all', u'Общее количество ДТП'),
)

accident_types = (
    ('driver', u'Нарушение ПДД водителями ТС', u'Violation of traffic rules by vehicle drivers',),
    ('drunk', u'Нарушение ПДД водителями ТС в состоянии алкогольного опьянения', u'Violation of traffic rules by vehicle drivers while intoxicated',),
    ('juridical', u'Нарушение ПДД водителями ТС юридических лиц', u'Violation of traffic rules by entity vehicle drivers',),
    ('physical', u'Нарушение ПДД водителями ТС физических лиц', u'Violation of traffic rules by individual vehicle drivers',),
    ('pedestrian', u'Нарушение ПДД пешеходами', u'Violation of traffic rules by pedestrians',),
    ('broken', u'ДТП из-за эксплуатации технически неисправных ТС', u'Accidents due to exploitation of technically faulty vehicles',),
    ('roads', u'ДТП из-за неудовлетворительного состояния улиц и дорог', u'Accidents due to the poor state of roads and streets',),
    ('hidden', u'ДТП с участием неустановленных транспортных средств', u'Road accidents involving unidentified vehicles',),
    ('all', u'Общее количество ДТП', u'Total number of road accidents',),
)

stat_types = (
    ('hurt', u'Число пострадавших', u'The number of victims', True),
    ('dead', u'Число погибших', u'The death toll', True),
    ('injured', u'Число раненых', u'The number of injured', True),
    ('accident', u'Число ДТП', u'The number of road accidents', False),
)

scale_types = (
    ('no', u'без масштаба', u'No', True),
    ('population', u'на 100 тыс. жителей', u'per 100,000 inhabitants', True),
    ('transport', u'на 10 тыс. транспортных средств', u'per 10,000 units of vehicles', False),
)

chart_types = (
    ('column', u'Вертикальная гистограмма', u'Column chart',),
    ('bar', u'Горизонтальная гистограмма', u'Bar chart',),
    ('area', u'Диаграмма с областями', u'Area chart',),
    ('line', u'Линейный график', u'Line chart',),
    ('point', u'Точечный график', u'Scatter chart',),
)

trend_types = (
    ('no', u'Нет', u'No',),
    ('linear', u'Линейная', u'Linear',),
    ('exponential', u'Экспоненциальная', u'Exponential',),
)

#sorted regions list in base loading order
regions = (
    u'Российская Федерация',
    u'Центральный округ',
    u'Северо-Западный округ',
    u'Южный округ',
    u'Приволжский округ',
    u'Уральский округ',
    u'Сибирский округ',
    u'Дальневосточный округ',
    u'Северо-Кавказский округ',
    u'Белгородская область',
    u'Брянская область',
    u'Владимирская область',
    u'Воронежская область',
    u'Ивановская область',
    u'Калужская область',
    u'Костромская область',
    u'Курская область',
    u'Липецкая область',
    u'г. Москва',
    u'Московская область',
    u'Орловская область',
    u'Рязанская область',
    u'Смоленская область',
    u'Тамбовская область',
    u'Тверская область',
    u'Тульская область',
    u'Ярославская область',
    u'Республика Карелия',
    u'Республика Коми',
    u'Архангельская область',
    u'Вологодская область',
    u'Калининградская область',
    u'Ленинград. обл. и г. С.-Петербург',
    u'Ленинградская область',
    u'г. С.-Петербург',
    u'Мурманская область',
    u'Новгородская область',
    u'Псковская область',
    u'Ненецкий авт.округ',
    u'Республика Адыгея',
    u'Республика Дагестан',
    u'Республика Ингушетия',
    u'Кабардино-Балкарская Республика',
    u'Республика Калмыкия',
    u'Карачаево-Черкесская Республика',
    u'Республика Северная Осетия',
    u'Чеченская Республика',
    u'Краснодарский край',
    u'Ставропольский край',
    u'Астраханская область',
    u'Волгоградская область',
    u'Ростовская область',
    u'Республика Башкортостан',
    u'Республика Марий Эл',
    u'Республика Мордовия',
    u'Республика Татарстан',
    u'Удмуртская Республика',
    u'Чувашская Республика',
    u'Пермский край',
    u'Пермская область',
    u'Кировская область',
    u'Нижегородская область',
    u'Оренбургская область',
    u'Пензенская область',
    u'Самарская область',
    u'Саратовская область',
    u'Ульяновская область',
    u'Коми-Пермяцкий авт.округ',
    u'Ханты-мансийский авт.округ - Югра',
    u'Курганская область',
    u'Свердловская область',
    u'Тюменская область',
    u'Челябинская область',
    u'Ханты-мансийский авт.округ',
    u'Ямало-ненецкий авт.округ',
    u'Республика Алтай',
    u'Республика Бурятия',
    u'Республика Тыва',
    u'Республика Хакасия',
    u'Алтайский край',
    u'Забайкальский край',
    u'Красноярский край',
    u'Иркутская область',
    u'Кемеровская область',
    u'Новосибирская область',
    u'Омская область',
    u'Томская область',
    u'Читинская область',
    u'Агинский бурятский авт.округ',
    u'Таймырский авт.округ',
    u'Усть-ордынский Бурятский авт.окр.',
    u'Эвенкийский авт.округ',
    u'Республика Саха (Якутия)',
    u'Приморский край',
    u'Хабаровский край',
    u'Амурская область',
    u'Камчатская область',
    u'Камчатский край',
    u'Магаданская область',
    u'Сахалинская область',
    u'Корякский авт. округ',
    u'Еврейская автономная область',
    u'Чукотский авт.округ',
    u'Чувашская Республика - Чувашия',
)


#keys - names of regions values - names of parent regions
parents = {
    u'Российская Федерация': None,
    u'Центральный округ': u'Российская Федерация',
    u'Северо-Западный округ': u'Российская Федерация',
    u'Южный округ': u'Российская Федерация',
    u'Приволжский округ': u'Российская Федерация',
    u'Уральский округ': u'Российская Федерация',
    u'Сибирский округ': u'Российская Федерация',
    u'Дальневосточный округ': u'Российская Федерация',
    u'Северо-Кавказский округ': u'Российская Федерация',

    u'Белгородская область': u'Центральный округ',
    u'Брянская область': u'Центральный округ',
    u'Владимирская область': u'Центральный округ',
    u'Воронежская область': u'Центральный округ',
    u'Ивановская область': u'Центральный округ',
    u'Калужская область': u'Центральный округ',
    u'Костромская область': u'Центральный округ',
    u'Курская область': u'Центральный округ',
    u'Липецкая область': u'Центральный округ',
    u'г. Москва': u'Центральный округ',
    u'Московская область': u'Центральный округ',
    u'Орловская область': u'Центральный округ',
    u'Рязанская область': u'Центральный округ',
    u'Смоленская область': u'Центральный округ',
    u'Тамбовская область': u'Центральный округ',
    u'Тверская область': u'Центральный округ',
    u'Тульская область': u'Центральный округ',
    u'Ярославская область': u'Центральный округ',

    u'Республика Карелия': u'Северо-Западный округ',
    u'Республика Коми': u'Северо-Западный округ',
    u'Архангельская область': u'Северо-Западный округ',
    u'Вологодская область': u'Северо-Западный округ',
    u'Калининградская область': u'Северо-Западный округ',
    u'Ленинград. обл. и г. С.-Петербург': u'Северо-Западный округ',

    u'Ленинградская область': u'Ленинград. обл. и г. С.-Петербург',
    u'г. С.-Петербург': u'Ленинград. обл. и г. С.-Петербург',

    u'Мурманская область': u'Северо-Западный округ',
    u'Новгородская область': u'Северо-Западный округ',
    u'Псковская область': u'Северо-Западный округ',
    u'Ненецкий авт.округ': u'Северо-Западный округ',

    u'Республика Адыгея': u'Южный округ',
    u'Республика Калмыкия': u'Южный округ',
    u'Краснодарский край': u'Южный округ',
    u'Астраханская область': u'Южный округ',
    u'Волгоградская область': u'Южный округ',
    u'Ростовская область': u'Южный округ',

    u'Республика Дагестан': u'Северо-Кавказский округ',
    u'Республика Ингушетия': u'Северо-Кавказский округ',
    u'Кабардино-Балкарская Республика': u'Северо-Кавказский округ',
    u'Карачаево-Черкесская Республика': u'Северо-Кавказский округ',
    u'Республика Северная Осетия': u'Северо-Кавказский округ',
    u'Чеченская Республика': u'Северо-Кавказский округ',
    u'Ставропольский край': u'Северо-Кавказский округ',

    u'Республика Башкортостан': u'Приволжский округ',
    u'Республика Марий Эл': u'Приволжский округ',
    u'Республика Мордовия': u'Приволжский округ',
    u'Республика Татарстан': u'Приволжский округ',
    u'Удмуртская Республика': u'Приволжский округ',
    u'Чувашская Республика': u'Приволжский округ',
    u'Чувашская Республика - Чувашия': u'Приволжский округ',
    u'Пермский край': u'Приволжский округ',
    u'Пермская область': u'Приволжский округ',
    u'Кировская область': u'Приволжский округ',
    u'Нижегородская область': u'Приволжский округ',
    u'Оренбургская область': u'Приволжский округ',
    u'Пензенская область': u'Приволжский округ',
    u'Самарская область': u'Приволжский округ',
    u'Саратовская область': u'Приволжский округ',
    u'Ульяновская область': u'Приволжский округ',
    u'Коми-Пермяцкий авт.округ': u'Приволжский округ',

    u'Ханты-мансийский авт.округ - Югра': u'Уральский округ',
    u'Курганская область': u'Уральский округ',
    u'Свердловская область': u'Уральский округ',
    u'Тюменская область': u'Уральский округ',
    u'Челябинская область': u'Уральский округ',
    u'Ханты-мансийский авт.округ': u'Уральский округ',
    u'Ямало-ненецкий авт.округ': u'Уральский округ',

    u'Республика Алтай': u'Сибирский округ',
    u'Республика Бурятия': u'Сибирский округ',
    u'Республика Тыва': u'Сибирский округ',
    u'Республика Хакасия': u'Сибирский округ',
    u'Алтайский край': u'Сибирский округ',
    u'Забайкальский край': u'Сибирский округ',
    u'Красноярский край': u'Сибирский округ',
    u'Иркутская область': u'Сибирский округ',
    u'Кемеровская область': u'Сибирский округ',
    u'Новосибирская область': u'Сибирский округ',
    u'Омская область': u'Сибирский округ',
    u'Томская область': u'Сибирский округ',
    u'Читинская область': u'Сибирский округ',
    u'Агинский бурятский авт.округ': u'Сибирский округ',
    u'Таймырский авт.округ': u'Сибирский округ',
    u'Усть-ордынский Бурятский авт.окр.': u'Сибирский округ',
    u'Эвенкийский авт.округ': u'Сибирский округ',

    u'Республика Саха (Якутия)': u'Дальневосточный округ',
    u'Приморский край': u'Дальневосточный округ',
    u'Хабаровский край': u'Дальневосточный округ',
    u'Амурская область': u'Дальневосточный округ',
    u'Камчатская область': u'Дальневосточный округ',
    u'Камчатский край': u'Дальневосточный округ',
    u'Магаданская область': u'Дальневосточный округ',
    u'Сахалинская область': u'Дальневосточный округ',
    u'Корякский авт. округ': u'Дальневосточный округ',
    u'Еврейская автономная область': u'Дальневосточный округ',
    u'Чукотский авт.округ': u'Дальневосточный округ',
}


def get_name(searched_type, types, lang, flag=False):
    for cur in types:
        if cur[0] == searched_type:
            if flag and not cur[3]:
                return None
            if lang == 'ru':
                return cur[1]
            return cur[2]
    return None


def get_accident_name_by_type(searched_accident_type, lang, flag=False):
    return get_name(searched_accident_type, accident_types, lang, flag)


def get_chart_name_by_type(searched_chart_type, lang, flag=False):
    return get_name(searched_chart_type, chart_types, lang, flag)


def get_stat_name_by_type(searched_stat_type, lang, flag=False):
    return get_name(searched_stat_type, stat_types, lang, flag)


def get_trend_name_by_type(searched_trend_type, lang):
    return get_name(searched_trend_type, trend_types, lang)


def get_scale_name_by_type(searched_scale_type, lang, flag=False):
    return get_name(searched_scale_type, scale_types, lang, flag)

