from django.core.management.base import BaseCommand, CommandError
from django.contrib.gis.utils import LayerMapping
from ...models import District

class Command(BaseCommand):
    help = 'Import models from shapefiles'

    def handle(self, *args, **options):
        path_of_shp = './shapefiles/District.shp'
        district_mapping = {
            'name': 'DISTNAME',
            'geom': 'POLYGON'
        }
        try:
            lm = LayerMapping(District, path_of_shp, district_mapping, transform=False)
            lm.save(strict=True, verbose=True)
            self.stdout.write(self.style.SUCCESS('Successfully imported District'))
        except:
            raise CommandError('Error importing District')
