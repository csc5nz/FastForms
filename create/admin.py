from django.contrib import admin
from .models import Documents
from .models import Bill_of_sale

# Register your models here.
admin.site.register(Documents)
admin.site.register(Bill_of_sale)