# Generated by Django 4.1.1 on 2022-12-10 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dailyreport', '0003_alter_dailyreportdb_pdf_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyreportdb',
            name='bhp',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=5, null=True),
        ),
    ]
