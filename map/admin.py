from django.contrib.gis import admin
from .models import Suco, Aldeia, District, Subdistrict, PhotoTimor, IstoriaViazen, CommentPhoto
from leaflet.admin import LeafletGeoAdmin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _


class SucoAdmin(admin.OSMGeoAdmin):
    list_display = ['name', 'subdistrict_name', 'district_name']
    list_filter = ['district_name', 'subdistrict_name']


class AldeiaAdmin(admin.OSMGeoAdmin):
    list_display = ['name']
    list_filter = ['name']


class DistrictAdmin(admin.OSMGeoAdmin):
    list_display = ['name']
    list_filter = ['name']


class SubdistrictAdmin(admin.OSMGeoAdmin):
    list_display = ['name']
    list_filter = ['name']


class TimorgisUserAdmin(UserAdmin):
    nonsuper_fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Admin access'), {'fields': ('is_active', 'is_staff', 'groups')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    def get_fieldsets(self, request, user=None):
        if user is None:
            return UserAdmin.add_fieldsets
        if not request.user.is_superuser:
            return self.nonsuper_fieldsets
        return UserAdmin.fieldsets

    def get_queryset(self, request):
        queryset = super(TimorgisUserAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            return queryset.exclude(is_superuser=True)
        return queryset


admin.site.register(Suco, SucoAdmin)
admin.site.register(Aldeia, AldeiaAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(Subdistrict, SubdistrictAdmin)
admin.site.register(IstoriaViazen)
admin.site.register(PhotoTimor)
admin.site.register(CommentPhoto)
admin.site.unregister(User)
admin.site.register(User, TimorgisUserAdmin)

admin.site.site_header = "Timor Journey %s" % (_("administration"))
