# Generated by Django 4.1.1 on 2022-12-09 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dailyreport', '0002_remove_dailyreportdb_cmf_remove_dailyreportdb_dp_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyreportdb',
            name='pdf_file',
            field=models.FileField(blank=True, null=True, upload_to='dailyreports/%Y/%m/%d'),
        ),
    ]
