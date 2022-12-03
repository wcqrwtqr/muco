# Generated by Django 4.1.1 on 2022-12-03 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('jobs', '0002_jobsdb_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='dailyreportdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operationdate', models.DateField(blank=True)),
                ('lastdayops', models.CharField(blank=True, max_length=2500, null=True)),
                ('nextdayops', models.CharField(blank=True, max_length=2500, null=True)),
                ('h2s', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('co2', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('oilrate', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('waterrate', models.IntegerField(blank=True, null=True)),
                ('dp', models.IntegerField(blank=True, null=True)),
                ('staticp', models.IntegerField(blank=True, null=True)),
                ('gasrate', models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True)),
                ('orifice', models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True)),
                ('cmf', models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True)),
                ('whp', models.IntegerField(blank=True, null=True)),
                ('todayproduced', models.IntegerField(blank=True, null=True)),
                ('totalproduction', models.IntegerField(blank=True, null=True)),
                ('wht', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('bsw', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('hz', models.IntegerField(blank=True, null=True)),
                ('flowduration', models.IntegerField(blank=True, null=True)),
                ('chokesize', models.IntegerField(blank=True, null=True)),
                ('supervisorname', models.CharField(max_length=200)),
                ('jobid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.jobsdb')),
            ],
            options={
                'ordering': ['operationdate'],
            },
        ),
    ]
