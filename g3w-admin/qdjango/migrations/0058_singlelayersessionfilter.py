# Generated by Django 2.2.16 on 2020-12-30 09:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('qdjango', '0057_auto_20201210_0715'),
    ]

    operations = [
        migrations.CreateModel(
            name='SingleLayerSessionFilter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sessionid', models.CharField(max_length=255)),
                ('token', models.CharField(max_length=47)),
                ('qgs_expr', models.TextField()),
                ('time_asked', models.DateTimeField(auto_now=True)),
                ('layer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qdjango.Layer')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]