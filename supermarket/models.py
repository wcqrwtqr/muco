from django.db import models

# Create your models here.


class supermarketdb(models.Model):
    productid = models.CharField(max_length=20, unique=True, blank=True, null=True)
    product_name = models.CharField(max_length=255, blank=False)
    product_category = models.CharField(max_length=100, null=False, blank=False)
    product_quantity = models.PositiveSmallIntegerField(null=False, blank=False)

    def __str__(self) -> str:
        return f"{self.productid} {self.product_name}"
