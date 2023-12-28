from django.db import models
from django.urls import reverse
from personnel.models import personneldb


class trainingdb(models.Model):
    training_date_start = models.DateField(null=True)
    training_type = models.CharField(max_length=200, null=True)
    training_name = models.CharField(max_length=200, null=True)
    training_date_expire = models.DateField(blank=True, null=True)
    training_cost = models.DecimalField(
        max_digits=8, null=True, decimal_places=2, blank=True
    )
    description = models.CharField(max_length=900, null=True, blank=True)
    attendees = models.ManyToManyField(personneldb)
    pdf_file = models.FileField(upload_to="training/%Y/%m/%d", null=True, blank=True)

    def get_absolute_url(self):
        """Get the url of the path
        Get the url of the path when the user click on the url
        Returns:
            url with id number
        """
        return reverse("training_detail", kwargs={"pk": self.pk})

    def get_next(self):
        next = trainingdb.objects.filter(pk__gt=self.pk).order_by("pk").first()
        if next:
            return next
        else:
            return trainingdb.objects.all().order_by("pk").first()

    def get_prev(self):
        next = trainingdb.objects.filter(pk__lt=self.pk).order_by("pk").last()
        if next:
            return next
        else:
            return trainingdb.objects.all().order_by("pk").last()

    def __str__(self):
        return "%s %s" % (self.training_name, self.training_date_start)

    class Meta:
        ordering = ["training_type"]
