# Generated by Django 4.1.1 on 2022-12-10 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dailyreport', '0005_alter_dailyreportdb_bhp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyreportdb',
            name='bhp',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
