from django.db import models
from django.urls import reverse
from personnel.models import personneldb
# Create your models here.

class trainingdb(models.Model):
    training_date_start  = models.DateField( null=True)
    training_type        = models.CharField(max_length=200, null=True)
    training_name        = models.CharField(max_length=200, null=True)
    training_date_expire = models.DateField(blank=True, null=True)
    training_cost       = models.DecimalField(max_digits=8, null=True,decimal_places=2,blank=True)
    # expiry_date = models.DateField(blank=True, null=True)
    # person = models.ForeignKey(personneldb,on_delete=models.CASCADE)
    description = models.CharField(max_length=900, null=True,blank=True)
    attendees = models.ManyToManyField(personneldb)
    # file_link = models.URLField(max_length=200, null=True, blank=True)

    def get_absolute_url(self):
        """Get the url of the path
        Get the url of the path when the user click on the url
        Returns:
            url with id number
        """
        return reverse ('training_detail',kwargs={'pk':self.pk})

    def __str__(self):
        return '%s %s' % (self.training_name,self.training_date_start)
    class Meta:
        ordering = ['training_type']
