# Generated by Django 4.1.1 on 2022-12-09 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personnel', '0004_alter_personneldb_pdf_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personneldb',
            name='pdf_file',
            field=models.FileField(blank=True, null=True, upload_to='pdfs/%Y/%m/%d'),
        ),
    ]
