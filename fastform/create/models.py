import datetime

from django.db import models
from django.utils import timezone


# Create your models here.
DOCUMENT_TYPES = (('', 'empty'), ('bill_of_sale', 'Bill of Sale'), ('articles_of_incorporation', 'Articles of Incorporation')) 

class Document(models.Model):
    doc_id = models.PositiveBigIntegerField("Document ID", default=0)
    doc_type = models.CharField("Document Type", max_length=200, blank=True, choices=DOCUMENT_TYPES, default='')
    # Document name should be Document01, 02 ... (need additional function)
    doc_name = models.CharField(max_length=20, default="Document name")
    doc_date = models.DateTimeField(default=timezone.now)

    
STATES =  (('', '- State -'), ('AL', 'Alabama'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming'))

class BillOfSale(models.Model):
    # Document name should be Document01, 02 ... (need additional function)
    document_name = models.CharField(max_length=20, default="Bill of Sale")
    document_date = models.DateTimeField(default=timezone.now)

    seller_name = models.CharField('Name', max_length=200, blank=True)
    seller_address = models.CharField('Address', max_length=200, blank=True)
    seller_city = models.CharField('City', max_length=200, blank=True)
    seller_state = models.CharField("State", max_length=200, blank=True, choices=STATES, default='')
    seller_zip = models.CharField('Zip', max_length=200, blank=True)

    buyer_name = models.CharField('Name', max_length=200, blank=True)
    buyer_address = models.CharField('Address', max_length=200, blank=True)
    buyer_city = models.CharField('City', max_length=200, blank=True)
    buyer_state = models.CharField('State', max_length=200, blank=True, choices=STATES, default='')
    buyer_zip = models.CharField('Zip', max_length=5, blank=True)

    properties = models.CharField(max_length=200, blank=True)
    price = models.CharField(max_length=20, blank=True)
    sale_date = models.DateField(default=timezone.now)


    def save(self, *args, **kwargs):
        new = False
        if not self.pk:  # object is being created, thus no primary key field yet
            new = True
            
        super(BillOfSale, self).save(*args, **kwargs)
        if new:
            document = Document.objects.create()
            document.doc_id = self.id
            document.doc_type = 'bill_of_sale'
            document.doc_name = self.document_name
            document.save()

    # def __str__(self):
    #     return 