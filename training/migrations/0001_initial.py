# Generated by Django 4.1.1 on 2022-11-11 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('personnel', '0002_alter_personneldb_department_alter_personneldb_grade_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='trainingdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('training_date_start', models.DateField(null=True)),
                ('training_type', models.CharField(max_length=200, null=True)),
                ('training_name', models.CharField(max_length=200, null=True)),
                ('training_date_expire', models.DateField(blank=True, null=True)),
                ('training_cost', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('description', models.CharField(blank=True, max_length=900, null=True)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personnel.personneldb')),
            ],
            options={
                'ordering': ['training_type'],
            },
        ),
    ]