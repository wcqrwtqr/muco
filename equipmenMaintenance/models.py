from django.db import models
from equipmentList.models import equipmentdb
from batteryList.models import batterydb
from django.urls import reverse

# Create your models here.

class Maintenancedb(models.Model):
    main_date_start = models.DateField( null=True)
    ms_type= models.CharField(max_length=20, null=True)
    main_date_end = models.DateField(blank=True, null=True)
    main_cost = models.DecimalField(max_digits=8, null=True,decimal_places=2,blank=True)
    expiry_date = models.DateField(blank=True, null=True)
    asset = models.ForeignKey(equipmentdb,on_delete=models.CASCADE)
    description = models.CharField(max_length=900, null=True,blank=True)
    file_link = models.URLField(max_length=200, null=True, blank=True)

    def get_absolute_url(self):
        """Get the url of the path
        Get the url of the path when the user click on the url
        Returns:
            url with id number
        """
        return reverse ('maintenance_detail',kwargs={'pk':self.pk})

    def __str__(self):
        return '%s %s %s' % (self.ms_type,self.main_date_start,self.asset)
    class Meta:
        ordering = ['asset']


class Batterymaintenancedb(models.Model):
    battery = models.ForeignKey(batterydb,on_delete=models.CASCADE)
    check_date= models.DateField( null=False)
    description = models.CharField(max_length=500, null=True,blank=True)
    ms_type= models.CharField(max_length=20, null=True)
    voltage_value = models.DecimalField(max_digits=4, null=True, decimal_places=2, blank=True)

    def get_absolute_url(self):
        """Get the url of the path
        Get the url of the path when the user click on the url
        Returns:
            url with id number
        """
        return reverse ('battery_maintenance_detail',kwargs={'pk':self.pk})

    @property
    def ops_status(self):
        if self.voltage_value > 3.1:
            return "Good"
        return "Not Good"

    def __str__(self):
        return '%s %s %s' % (self.ms_type,self.check_date, self.battery)
    class Meta:
        ordering = ['check_date']
