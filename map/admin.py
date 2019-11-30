from django.contrib.gis import admin
from .models import Suco, Aldeia


class SucoAdmin(admin.OSMGeoAdmin):
    list_display = ['name', 'subdistrict_name', 'district_name']
    list_filter = ['district_name', 'subdistrict_name']


class AldeiaAdmin(admin.OSMGeoAdmin):
    list_display = ['name', 'descriptio_name', 'id_aldeia_name', 'dist_code_name']
    list_filter = ['name', 'descriptio_name']

admin.site.register(Suco, SucoAdmin)
admin.site.register(Aldeia, AldeiaAdmin)

