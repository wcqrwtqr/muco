from django.db import models
from django.urls import reverse
# Create your models here.

class marketingdb(models.Model):
    meeting_date  = models.DateField(null=True, blank=True)
    meeting_type = models.CharField(max_length=200, unique=False, blank=True)
    meeting_description = models.CharField(max_length=800, null=True, blank=True)
    departement = models.CharField(max_length=4, null=True, blank=True)
    client = models.CharField(max_length=200, unique=False, blank=True)
    attendance = models.CharField(max_length=200, unique=False, blank=True)
    # asset_life = models.IntegerField(null=True, blank=True)
    # acquisition_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    # pdf_file = models.FileField(upload_to='equipment/%Y/%m/%d', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('market_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return '%s %s %s'% (self.client, self.meeting_type, self.meeting_date)

    def get_next(self):
        next = marketingdb.objects.filter(pk__gt=self.pk).order_by('pk').first()
        if next:
            return next
        else:
            return marketingdb.objects.all().order_by('pk').first()

    def get_prev(self):
        next = marketingdb.objects.filter(pk__lt=self.pk).order_by('pk').last()
        if next:
            return next
        else:
            return marketingdb.objects.all().order_by('pk').last()

    class Meta:
        ordering = ['meeting_date']
