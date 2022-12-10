from jobs.models import jobsdb
from django.db import models
from django.urls import reverse

class dailyreportdb(models.Model):

    jobid = models.ForeignKey(jobsdb,on_delete=models.CASCADE)
    operationdate  = models.DateField(null=False, blank=True)
    lastdayops = models.CharField(max_length=2500, null=True, blank=True)
    nextdayops = models.CharField(max_length=2500, null=True, blank=True)
    h2s = models.DecimalField(max_digits=5,decimal_places=2,blank=True,null=True)
    co2 = models.DecimalField(max_digits=5,decimal_places=2,blank=True,null=True)
    oilrate = models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True)
    waterrate = models.IntegerField(blank=True,null=True)
    gasrate = models.DecimalField(max_digits=10,decimal_places=4,blank=True,null=True)
    whp = models.IntegerField(blank=True,null=True)
    wht = models.DecimalField(max_digits=5,decimal_places=2,blank=True,null=True)
    # bhp = models.DecimalField(max_digits=5,decimal_places=2,blank=True,null=True)
    bhp = models.IntegerField(blank=True,null=True)
    bht = models.DecimalField(max_digits=5,decimal_places=2,blank=True,null=True)
    bsw = models.DecimalField(max_digits=5,decimal_places=2,blank=True,null=True)
    hz = models.IntegerField(blank=True,null=True)
    chokesize = models.IntegerField(blank=True,null=True)
    supervisorname = models.CharField(max_length=200,  blank=False)
    pdf_file = models.FileField(upload_to='dailyreports/%Y/%m/%d', null=True, blank=True)

    @property
    def calc_gor(self):
        x = int(self.gasrate / self.oilrate * 1000000)
        return x

    def get_next(self):
        next = dailyreportdb.objects.filter(pk__gt=self.pk).order_by('pk').first()
        if next:
            return next
        # If the current card is the last one, return the first card in the deck
        else:
            return dailyreportdb.objects.all().order_by('pk').first()

    def get_prev(self):
        next = dailyreportdb.objects.filter(pk__lt=self.pk).order_by('pk').last()
        if next:
            return next
        # If the current card is the last one, return the first card in the deck
        else:
            return dailyreportdb.objects.all().order_by('pk').last()

    def get_absolute_url(self):
        return reverse('dailyreport_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return '%s %s %s'% (self.jobid, self.operationdate, self.supervisorname)
    class Meta:
        ordering = ['operationdate']
