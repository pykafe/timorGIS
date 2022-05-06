from django.core.management.base import BaseCommand, CommandError
from map.models import  PhotoTimor
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile


class Command(BaseCommand):
    help = 'Import models from PhotoTimor'

    def handle(self, *args, **options):
        try:
            for photo in PhotoTimor.objects.all():
                image_pil = Image.open(photo.image)
                image_pil.thumbnail((450, 200))
                new_image_io = BytesIO()
                image_pil.save(new_image_io, format="JPEG")
                image_name = f"{image_pil.width}_{image_pil.height}_{photo.image.name}"
                photo.image_thumbnail.save(image_name, content=ContentFile(new_image_io.getvalue()), save=False)
                photo.save()
            self.stdout.write(self.style.SUCCESS('Successfully imported PhotoTimor'))
        except:
            raise CommandError('Error importing PhotoTimor')
