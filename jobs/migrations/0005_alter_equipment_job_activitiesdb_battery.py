# Generated by Django 4.1.1 on 2022-12-05 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('batteryList', '0003_alter_batterydb_in_service_date'),
        ('jobs', '0004_equipment_job_activitiesdb_battery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment_job_activitiesdb',
            name='battery',
            field=models.ManyToManyField(blank=True, to='batteryList.batterydb'),
        ),
    ]
