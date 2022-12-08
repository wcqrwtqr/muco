# Generated by Django 4.1.1 on 2022-12-08 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipmenMaintenance', '0002_batterymaintenancedb'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='maintenancedb',
            name='file_link',
        ),
        migrations.AddField(
            model_name='batterymaintenancedb',
            name='pdf_file',
            field=models.FileField(blank=True, null=True, upload_to='batteryMaintenance/'),
        ),
        migrations.AddField(
            model_name='maintenancedb',
            name='pdf_file',
            field=models.FileField(blank=True, null=True, upload_to='maintenance/'),
        ),
    ]