from django.contrib.gis import admin
from .models import Suco, Aldeia, District


class SucoAdmin(admin.OSMGeoAdmin):
    list_display = ['name', 'subdistrict_name', 'district_name']
    list_filter = ['district_name', 'subdistrict_name']


class AldeiaAdmin(admin.OSMGeoAdmin):
    list_display = ['name']
    list_filter = ['name']

    
class DistrictAdmin(admin.OSMGeoAdmin):
    list_display = ['name']
    
   
admin.site.register(Suco, SucoAdmin)
admin.site.register(Aldeia, AldeiaAdmin)
admin.site.register(District, DistrictAdmin)