# Generated by Django 2.2.10 on 2020-04-04 02:37

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0008_auto_20200404_0226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='istoriaviazen',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='istoria', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='istoriaviazen',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 4, 2, 37, 17, 219640, tzinfo=utc)),
        ),
    ]