# from django.contrib.admin.options import transaction
from django.db import models
from equipmentList.models import equipmentdb
from batteryList.models import batterydb
from django.urls import reverse
# from equipmentList.models import EQUIPMENT_DB
# import datetime
# Create your models here.

class jobsdb(models.Model):
    jobid = models.CharField(max_length = 20 ,unique=True,blank=True, null=True)
    client = models.CharField(max_length=255,blank=False)
    field = models.CharField(max_length=255,blank=True, null=True)
    well = models.CharField(max_length=255,blank=False, null=True)
    country = models.CharField(max_length=255,blank=False,default='Iraq')
    departmenet = models.CharField(max_length= 10, default='WSS', null=True, blank=True)
    service = models.CharField(max_length= 50, default='Eco meter', null=True, blank=True)
    description = models.CharField(max_length= 800, blank=True, null=True)
    startDate = models.DateField(null=True, blank=True)
    endDate = models.DateField(blank=True,null=True)
    # isContract = models.BooleanField(default=True, null=True, blank=True)
    # BL = models.CharField(max_length= 3, default='SWT', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('jobs_detail',kwargs={'pk':self.pk})

    def __str__(self):
        return '%s %s %s'% (self.client, self.well, self.startDate)


    def get_next(self):
        next = jobsdb.objects.filter(pk__gt=self.pk).order_by('pk').first()
        if next:
            return next
        else:
            return jobsdb.objects.all().order_by('pk').first()

    def get_prev(self):
        next = jobsdb.objects.filter(pk__lt=self.pk).order_by('pk').last()
        if next:
            return next
        else:
            return jobsdb.objects.all().order_by('pk').last()

    def get_absolute_url(self):
        return reverse('battery_detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['client']

class equipment_job_activitiesdb(models.Model):
    jobidnew  = models.ForeignKey(jobsdb,on_delete=models.CASCADE)
    assetnew  = models.ForeignKey(equipmentdb, on_delete=models.CASCADE, null=False)
    battery  = models.ManyToManyField(batterydb, blank=True)

    def get_absolute_url(self):
        return reverse('equipment_jobs_detail',kwargs={'pk':self.pk})

    def __str__(self):
        return '%s %s'% (self.jobidnew, self.assetnew)

    def get_next(self):
        next = equipment_job_activitiesdb.objects.filter(pk__gt=self.pk).order_by('pk').first()
        if next:
            return next
        else:
            return equipment_job_activitiesdb.objects.all().order_by('pk').first()

    def get_prev(self):
        next = equipment_job_activitiesdb.objects.filter(pk__lt=self.pk).order_by('pk').last()
        if next:
            return next
        else:
            return equipment_job_activitiesdb.objects.all().order_by('pk').last()

    def get_absolute_url(self):
        return reverse('battery_detail', kwargs={'pk': self.pk})


    class Meta:
        ordering = ['jobidnew']
