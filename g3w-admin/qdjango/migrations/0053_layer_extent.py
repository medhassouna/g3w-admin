# Generated by Django 2.2.13 on 2020-09-30 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qdjango', '0052_layer_download_csv'),
    ]

    operations = [
        migrations.AddField(
            model_name='layer',
            name='extent',
            field=models.TextField(blank=True, null=True, verbose_name='Layer extension'),
        ),
    ]