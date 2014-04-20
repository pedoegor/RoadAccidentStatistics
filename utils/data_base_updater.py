# -*- coding: utf-8 -*-
from RoadAccidentStatistics.views import *
from RoadAccidentStatistics.models import *
import finland_stats
import sys
import xlrd


reload(sys)
sys.setdefaultencoding('utf-8')

#period
from_year = 2004
to_year = 2013


#boolean list that indicates regions that are included in current .xls file
active_regions_list = []


#checks if input region name is correct
def if_region_identified(name):
    return name in parents.keys()


#gets parent region name
def get_parent_name(name):
    return parents[name]


#return result_list that contains numbers of 'абс.' columns
def get_proper_columns(file_name, table_number):
    result_list = []

    xls_file = xlrd.open_workbook(file_name, formatting_info=True)
    table = xls_file.sheet_by_index(table_number)

    for row in range(0, 5):

        for column in range(0, table.ncols - 1):

            cell_value = str(table.cell_value(row, column)).replace('*', '')
            text_in_cell = cell_value.strip()

            if text_in_cell == u'абс.':
                result_list.append(column)

        if result_list:
            return result_list


#function that drops database
def drop_db():
    #drop current base
    RegionStat.objects.all().delete()
    RegionCrashedTransport.objects.all().delete()
    RegionPopulation.objects.all().delete()
    Region.objects.all().delete()


#cast to int
def cast_int(string):
    try:
        value = int(string)
        return value
    except ValueError:
        return 0


#cast to float
def cast_float(string):
    try:
        value = float(string)
        return value
    except ValueError:
        return 0.0


#load regions structure from parents to base
def load_regions_db():
    for region in regions:
        #print region
        Region.objects.create(name=region, parent=get_region_by_name(parents.get(region)))

        active_regions_list.append(False)


#loads to db info about regions (ONLY REASON TABLES) from .xls
def load_region_reason_db(file_name_with_path, table_index, year):
    columns = get_proper_columns(file_name_with_path, table_index)

    xls_file_object = xlrd.open_workbook(file_name_with_path, formatting_info=True)
    sheet = xls_file_object.sheet_by_index(table_index)
    reason = reasons[table_index]

    #if table is number  0 then we should set list of active regions
    if table_index == 0:

        #set active regions list for .xls to [False, False, ...]
        for i in range(len(active_regions_list)):
            active_regions_list[i] = False

    for row in range(4, sheet.nrows):

        #get region name
        name = str(sheet.cell_value(row, 0)).replace('*', '').strip()
        if not if_region_identified(name):
            continue

        #set region as active
        if table_index == 0:
            active_regions_list[regions.index(name)] = True

        #load region statistics
        RegionStat.objects.create(region=get_region_by_name(name),
                                  year=year,
                                  accident_type=reason,
                                  dead_number=cast_int(sheet.cell_value(row, columns[1])),
                                  injured_number=cast_int(sheet.cell_value(row, columns[2])),
                                  accident_number=cast_int(sheet.cell_value(row, columns[0])))

        if name == u'Дальневосточный округ':
            break

            #now load data for regions that are not active in current .xls
    for i in range(len(active_regions_list)):
        if not active_regions_list[i]:
            RegionStat.objects.create(region=get_region_by_name(regions[i]),
                                      year=year,
                                      accident_type=reason,
                                      dead_number=0,
                                      injured_number=0,
                                      accident_number=0)


#IN THIS METHOD YOU SHOULD SET YOUR EXPRESSION !!!!!!!!!! NICK !!!!! DO YOU HEAR ME????!!!!!!!!!!!!!!!!
#loads region statistics about population and accidents (ONLY TABLE # 1)
def load_region_transport_and_population_db(file_name_with_path, table_index, year):
    columns = get_proper_columns(file_name_with_path, table_index)

    xls_file_object = xlrd.open_workbook(file_name_with_path, formatting_info=True)
    sheet = xls_file_object.sheet_by_index(table_index)

    all_stat_data = RegionStat.objects.filter(year=year, accident_type='all').all()
    for row in range(4, sheet.nrows):

        #get region name
        name = str(sheet.cell_value(row, 0)).replace('*', '').strip()

        if not if_region_identified(name):
            continue

        region = get_region_by_name(name)
        region_stat = all_stat_data.filter(region=region)[0]

        #load region POPULATION
        cell_value = cast_float(sheet.cell_value(row, columns[1]))
        RegionPopulation.objects.create(region=region,
                                        year=year,
                                        population=(0 if cell_value == 0.0
                                                    else region_stat.get_stat_number('hurt') * 100000 / cell_value))

        #load region TRANSPORT
        cell_value = cast_float(sheet.cell_value(row, columns[0]))
        RegionCrashedTransport.objects.create(region=region,
                                              year=year,
                                              crashed_transport_number=(
                                                  0 if cell_value == 0.0 else region_stat.accident_number * 10000 / cell_value))
        if name == u'Дальневосточный округ':
            break

    #now load data for regions that are not active in current .xls
    for i in range(len(active_regions_list)):
        if not active_regions_list[i]:
            region = get_region_by_name(regions[i])

            RegionPopulation.objects.create(region=region,
                                            year=year,
                                            population=0)

            RegionCrashedTransport.objects.create(region=region,
                                                  year=year,
                                                  crashed_transport_number=0)


#WARNING DONT START IF NOT SURE TOOOOO MUCH TIME WORKS
#method that load all data from downloaded .xls to database (CURRENT DATA DROPS!!!!)
def update_db():
    #drop current base
    drop_db()

    print " ===================================Finland Stats==================================================="
    finland_stats.add_stats()
    print " ===================================Finland Stats: OK==============================================="

    #create region structure in the base
    load_regions_db()

    #load from xls to base
    for year in range(from_year, to_year + 1):

        file_name = "tables/" + str(year) + ".xls"

        print " ===================================" + file_name + "==================================================="

        #get data from file by REASONS
        for table in reason_table_numbers:
            load_region_reason_db(file_name, table, year)

        print ("data by REASONS: OK")

        #get data from file: POPULATION AND TRANSPORT
        load_region_transport_and_population_db(file_name, 1, year)

        print ("data: POPULATION AND TRANSPORT: OK")

        print " ===================================" + file_name + ": OK==============================================="

    print "------------------------------------------------------------------------------------------------------------"
    print "-------------------------------------------LOAD STATUS: OK--------------------------------------------------"
    print "------------------------------------------------------------------------------------------------------------"

# index on region names
# create unique index if not exists region_index on RoadAccidentStatistics_region(name)