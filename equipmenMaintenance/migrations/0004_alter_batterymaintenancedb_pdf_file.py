# Generated by Django 4.1.1 on 2022-12-09 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipmenMaintenance', '0003_remove_maintenancedb_file_link_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batterymaintenancedb',
            name='pdf_file',
            field=models.FileField(blank=True, null=True, upload_to='batteryMaintenance/%Y/%m/%d'),
        ),
    ]
