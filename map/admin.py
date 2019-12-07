from django.contrib.gis import admin
from .models import Suco, District


class SucoAdmin(admin.OSMGeoAdmin):
    list_display = ['name', 'subdistrict_name', 'district_name']
    list_filter = ['district_name', 'subdistrict_name']


class DistrictAdmin(admin.OSMGeoAdmin):
    list_display = ['name']


admin.site.register(Suco, SucoAdmin)
admin.site.register(District, DistrictAdmin)

