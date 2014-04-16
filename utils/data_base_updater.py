# -*- coding: utf-8 -*-


from RoadAccidentStatistics.models import *
from RoadAccidentStatistics.views import *


from chart_support_types import *


import sys
import xlrd


reload(sys)
sys.setdefaultencoding('utf-8')


#checks if input region name is correct
def if_region_identified(name):
    return name in regions_and_parents.keys()


#gets parent region name
def get_parent_name(name):
    return regions_and_parents[name]


#period
from_year = 2004
to_year = 2013


#boolean list that indicates regions that are included in current .xls file
active_regions_list = []


#return result_list that contains numbers of 'абс.' columns
def get_proper_columns(file_name, table_number):

    result_list = []

    file = xlrd.open_workbook(file_name, formatting_info=True)
    table = file.sheet_by_index(table_number)

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


#load regions structure from regions_and_parents to base
def load_regions_db():
    for region in regions:
        #print region
        new_region = Region()
        new_region.name = region
        new_region.parent = None

        if not (parents[region] is None):
            new_region.parent = get_region_by_name(parents[region])

        new_region.save()

        active_regions_list.append(False)


#loads to db info about regions (ONLY REASON TABLES) from .xls ||||  file -  path & name of .xls, table - table number, year - year
def load_region_reason_db(file, table, year):

    columns = get_proper_columns(file, table)

    f = xlrd.open_workbook(filee, formatting_info=True)
    t = f.sheet_by_index(table)

    #if table is number  0 then we should set list of active regions
    if table == 0:

        #set active regions list for .xls to [False, False, ...]
        for i in range(0, len(active_regions_list)):
            active_regions_list[i] = False

        for row in range(4, t.nrows):

            #get region name
            c0 = str(t.cell_value(row, 0)).replace('*', '')
            name = c0.strip()

            if not if_region_identified(name):
                continue

            #set region as active
            index = regions.index(name)
            active_regions_list[index] = True

            #load region statistics
            stat = RegionStat()

            stat.region = get_region_by_name(name)
            stat.year = year
            stat.accident_type = reasons[table]
            stat.dead_number = cast_int(t.cell_value(row, columns[1]))
            stat.injured_number = cast_int(t.cell_value(row, columns[2]))
            stat.accident_number = cast_int(t.cell_value(row, columns[0]))

            stat.save()

            if name == u'Дальневосточный округ':
                break

        #now load data for regions that are not active in current .xls
        for i in range(0, len(active_regions_list)):
            if not active_regions_list[i]:

                stat = RegionStat()

                stat.region = get_region_by_name(regions[i])
                stat.year = year
                stat.accident_type = reasons[table]
                stat.dead_number = 0
                stat.injured_number = 0
                stat.accident_number = 0

                stat.save()

    else:

        for row in range(4, t.nrows):

            #get region name
            c0 = str(t.cell_value(row, 0)).replace('*', '')
            name = c0.strip()

            if not if_region_identified(name):
                continue

            #load region statistics
            stat = RegionStat()

            stat.region = get_region_by_name(name)
            stat.year = year
            stat.accident_type = reasons[table]
            stat.dead_number = cast_int(t.cell_value(row, columns[1]))
            stat.injured_number = cast_int(t.cell_value(row, columns[2]))
            stat.accident_number = cast_int(t.cell_value(row, columns[0]))

            stat.save()

            if name == u'Дальневосточный округ':
                break


        #now load data for regions that are not active in current .xls
        for i in range(0, len(active_regions_list)):
            if not active_regions_list[i]:

                stat = RegionStat()

                stat.region = get_region_by_name(regions[i])
                stat.year = year
                stat.accident_type = reasons[table]
                stat.dead_number = 0
                stat.injured_number = 0
                stat.accident_number = 0

                stat.save()


#IN THIS METHOD YOU SHOULD SET YOUR EXPRESSION !!!!!!!!!! NICK !!!!! DO YOU HEAR ME????!!!!!!!!!!!!!!!!
#loads region statistics about population and accidents (ONLY TABLE # 1) ||||  file -  path & name of .xls, table - table number, year - year
def load_region_transport_and_population_db(file, table, year):

    columns = get_proper_columns(file, table)

    f = xlrd.open_workbook(filee, formatting_info=True)
    t = f.sheet_by_index(table)


    for row in range(4, t.nrows):

        #get region name
        c0 = str(sheet.cell_value(row, 0)).replace('*', '')
        name = c0.strip()

        if not if_region_identified(name):
            continue

        #load region POPULATION
        population = RegionPopulation()

        population.region = get_region_by_name(name)
        population.year = year
        population.population = 0 #HERE YOUR EXPRESSION DADA FROM TABLE THAT YOU NEED IS :  cast_float(t.cell_value(row, columns[0]))

        population.save()

        #load region TRANSPORT
        transport = RegionCrashedTransport()

        transport.region = population.region
        transport.year = year
        transport.crashed_transport_number = 0 #HERE YOUR EXPRESSION DADA FROM TABLE THAT YOU NEED IS :  cast_float(t.cell_value(row, columns[1]))

        transport.save()

        if name == u'Дальневосточный округ':
                break


    #now load data for regions that are not active in current .xls
    for i in range(0, len(active_regions_list)):
        if not active_regions_list[i]:

            #load region POPULATION
            population = RegionPopulation()

            population.region = get_region_by_name(regions[i])
            population.year = year
            population.population = 0

            population.save()

            #load region TRANSPORT
            transport = RegionCrashedTransport()

            transport.region = population.region
            transport.year = year
            transport.crashed_transport_number = 0

            transport.save()


#WARNING DONT START IF NOT SURE TOOOOO MUCH TIME WORKS
#method that load all data from downloaded .xls to database (CURRENT DATA DROPS!!!!)
def update_db():

    #drop current base
    drop_db()


    #create region structure in the base
    load_regions_db()

    #load from xls to base
    for year in range(from_year, to_year):

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
