# Generated by Django 4.1.1 on 2022-12-03 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='jobsdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobid', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('client', models.CharField(max_length=255)),
                ('field', models.CharField(blank=True, max_length=255, null=True)),
                ('well', models.CharField(max_length=255, null=True)),
                ('country', models.CharField(default='Iraq', max_length=255)),
                ('departmenet', models.CharField(blank=True, default='WSS', max_length=10, null=True)),
                ('description', models.CharField(blank=True, max_length=800, null=True)),
                ('startDate', models.DateField(blank=True, null=True)),
                ('endDate', models.DateField(blank=True, null=True)),
            ],
            options={
                'ordering': ['client'],
            },
        ),
    ]