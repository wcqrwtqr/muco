from django.contrib import admin
from .models import jobsdb, equipment_job_activitiesdb
# Register your models here.

admin.site.register(jobsdb)
admin.site.register(equipment_job_activitiesdb)
