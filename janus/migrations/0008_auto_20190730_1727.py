# Generated by Django 2.1.10 on 2019-07-30 15:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('janus', '0007_auto_20190131_2348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationextension',
            name='application',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='extension', to=settings.OAUTH2_PROVIDER_APPLICATION_MODEL),
        ),
    ]
