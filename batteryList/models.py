from django.db import models
from django.urls import reverse

class batterydb(models.Model):
    part_num = models.CharField(max_length=40, unique=False, blank=True)
    serial_num = models.CharField(max_length=20, unique=True, blank=True)
    description = models.CharField(max_length=400, null=True, blank=True)
    purchase_date  = models.DateField(null=True, blank=True)
    in_service_date  = models.DateField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('battery_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return '%s %s %s'% (self.serial_num, self.part_num, self.description)
    class Meta:
        ordering = ['serial_num']
