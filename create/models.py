import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Documents(models.Model):
    bill_of_sale = models.ForeignKey('Bill_of_sale', on_delete=models.CASCADE,)

#
class Bill_of_sale(models.Model):
    document_name = models.CharField(max_length=20, default="Document name")
    document_date = models.DateTimeField(default=timezone.now)

    seller_name = models.CharField(max_length=200)
    seller_address = models.CharField(max_length=200)
    seller_city = models.CharField(max_length=200)
    seller_state = models.CharField(max_length=200)
    seller_zip = models.CharField(max_length=200)

    buyer_name = models.CharField(max_length=200)
    buyer_address = models.CharField(max_length=200)
    buyer_city = models.CharField(max_length=200)
    buyer_state = models.CharField(max_length=200)
    buyer_zip = models.CharField(max_length=5)

    properties = models.CharField(max_length=200)
    price = models.CharField(max_length=20)

    sale_date = models.DateField(default=timezone.now)

    


    def __str__(self):
        return 