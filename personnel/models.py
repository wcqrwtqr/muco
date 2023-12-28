from django.db import models
from django.urls import reverse


class personneldb(models.Model):
    first_name = models.CharField(max_length=255, blank=False)
    last_name = models.CharField(max_length=255, blank=False)
    senionrty_date = models.DateField(null=False, blank=True)
    birth_date = models.DateField(null=False, blank=True)
    grade = models.CharField(max_length=255, blank=False)
    position = models.CharField(max_length=255, blank=False)
    department = models.CharField(max_length=255, blank=False)
    pdf_file = models.FileField(upload_to="pdfs/%Y/%m/%d", null=True, blank=True)

    def get_absolute_url(self):
        return reverse("personnel_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return "%s %s %s" % (self.first_name, self.last_name, self.department)

    def get_next(self):
        next = personneldb.objects.filter(pk__gt=self.pk).order_by("pk").first()
        if next:
            return next
        else:
            return personneldb.objects.all().order_by("pk").first()

    def get_prev(self):
        next = personneldb.objects.filter(pk__lt=self.pk).order_by("pk").last()
        if next:
            return next
        else:
            return personneldb.objects.all().order_by("pk").last()

    class Meta:
        ordering = ["first_name"]
