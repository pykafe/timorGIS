from django.core.management.base import BaseCommand, CommandError
from django.contrib.gis.utils import LayerMapping
from ...models import Subdistrict

class Command(BaseCommand):
    help = 'Import models from shapefiles'

    def handle(self, *args, **options):
        path_of_shp = './shapefiles/subdistricts.shp'
        subdistrict_mapping = {
            'name': 'SUBDISTR',
            'geom': 'POLYGON'
        }
        try:
            lm = LayerMapping(Subdistrict, path_of_shp, subdistrict_mapping, transform=False)
            lm.save(strict=True, verbose=True)
            self.stdout.write(self.style.SUCCESS('Successfully imported Subdistrict'))
        except:
            raise CommandError('Error importing Subdistrict')
