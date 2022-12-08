from django.db import models
from django.urls import reverse

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
    pdf_file = models.FileField(upload_to='pdfs/', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('personnel_detail',kwargs={'pk':self.pk})

    def __str__(self):
        return '%s %s %s'% (self.first_name, self.last_name, self.department)

    class Meta:
        ordering = ['first_name']
