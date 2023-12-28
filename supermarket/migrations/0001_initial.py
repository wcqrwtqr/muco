# Generated by Django 4.1.1 on 2023-10-03 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='supermarketdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productid', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('product_name', models.CharField(max_length=255)),
                ('product_category', models.CharField(max_length=100)),
                ('product_quantity', models.PositiveSmallIntegerField()),
            ],
        ),
    ]
