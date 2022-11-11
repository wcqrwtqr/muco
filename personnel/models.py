from django.db import models

# Create your models here.

class personneldb(models.Model):
    # JOBID = models.CharField(max_length = 20 ,unique=True,blank=False)
    first_name = models.CharField(max_length=255,blank=False)
    last_name = models.CharField(max_length=255,blank=False)
    senionrty_date = models.DateField(null=False, blank=True)
    birth_date = models.DateField(null=False, blank=True)
    grade = models.CharField(max_length=255,blank=False)
    position = models.CharField(max_length=255,blank=False)
    department = models.CharField(max_length=255,blank=False)
    # field = models.CharField(max_length=255,blank=True, null=True)
    # well = models.CharField(max_length=255,blank=False, null=True)
    # country = models.CharField(max_length=255,blank=False,default='Iraq')
    # BU = models.CharField(max_length= 3, default='KIU', null=True, blank=True)
    # BL = models.CharField(max_length= 3, default='SWT', null=True, blank=True)
    # description = models.CharField(max_length= 800, blank=True, null=True)
    # isContract = models.BooleanField(default=True, null=True, blank=True)
    # startDate = models.DateField(null=True, blank=True)
    # endDate = models.DateField(blank=True,null=True)
    # h2s = models.DecimalField(max_digits=3,decimal_places=2,blank=True,null=True)
    # co2 = models.DecimalField(max_digits=3,decimal_places=2,blank=True,null=True)
    # oilRate = models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True)
    # gasRate = models.DecimalField(max_digits=10,decimal_places=3,blank=True,null=True)

    def get_absolute_url(self):
        return reverse('personnel_detail',kwargs={'pk':self.pk})

    def __str__(self):
        return '%s %s %s'% (self.first_name, self.last_name, self.department)

    class Meta:
        ordering = ['first_name']
