from django.core.management.base import BaseCommand, CommandError
from django.contrib.gis.utils import LayerMapping
from map.models import Aldeia

class Command(BaseCommand):
    help = 'Import models from shapefiles'

    def handle(self, *args, **options):
        path_of_shp = './shapefiles/Aldeia.shp'
        aldeia_mapping = {
            'name': 'Name',
            'geom': 'POINT'
        }
        try:
            lm = LayerMapping(Aldeia, path_of_shp, aldeia_mapping, transform=False)
            lm.save(strict=True, verbose=True)
            self.stdout.write(self.style.SUCCESS('Successfully imported Aldeia'))
        except:
            raise CommandError('Error importing Aldeia')
