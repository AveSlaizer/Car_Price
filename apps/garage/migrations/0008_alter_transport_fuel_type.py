# Generated by Django 4.2.5 on 2023-09-23 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('garage', '0007_alter_transport_brand_alter_transport_engine_power_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transport',
            name='fuel_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='garage.fueltype', verbose_name='Топливо'),
        ),
    ]
