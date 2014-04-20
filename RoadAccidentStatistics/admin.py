from django.contrib import admin
from models import *


class RegionAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')
    search_fields = ('name', 'parent__name')


class RegionPopulationAdmin(admin.ModelAdmin):
    list_display = ('region', 'year', 'population', )
    search_fields = ('region__name', 'year',)
    list_filter = ('year', 'region__name',)
    ordering = ('-year', 'region__name', )

class RegionCrashedTransportAdmin(admin.ModelAdmin):
    list_display = ('region', 'year', 'crashed_transport_number', )
    search_fields = ('region__name', 'year',)
    list_filter = ('year', 'region__name',)
    ordering = ('-year', 'region__name', )


class RegionStatAdmin(admin.ModelAdmin):
    list_display = ('region', 'year', 'accident_type', 'dead_number', 'injured_number', 'accident_number',)
    search_fields = ('region__name', 'year',)
    list_filter = ('year', 'region__name',)
    ordering = ('-year', 'region__name', )


admin.site.register(Region, RegionAdmin)
admin.site.register(RegionPopulation, RegionPopulationAdmin)
admin.site.register(RegionStat, RegionStatAdmin)
admin.site.register(RegionCrashedTransport, RegionCrashedTransportAdmin)