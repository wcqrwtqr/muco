# Generated by Django 4.1.1 on 2022-12-09 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipmentList', '0002_remove_equipmentdb_file_link_equipmentdb_pdf_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipmentdb',
            name='pdf_file',
            field=models.FileField(blank=True, null=True, upload_to='equipment/%Y/%m/%d'),
        ),
    ]
