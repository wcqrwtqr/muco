# Generated by Django 4.1.1 on 2022-11-11 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personnel', '0002_alter_personneldb_department_alter_personneldb_grade_and_more'),
        ('training', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainingdb',
            name='person',
        ),
        migrations.AddField(
            model_name='trainingdb',
            name='attendees',
            field=models.ManyToManyField(to='personnel.personneldb'),
        ),
    ]
