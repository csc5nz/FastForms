from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.clickjacking import xframe_options_sameorigin

# Create your views here.

def bill_of_sale(request):
    template = loader.get_template('create/build_bill_of_sale_01.html')
    context = {}

    return HttpResponse(template.render(context, request))

@xframe_options_exempt
def view_bill_of_sale(request):
    template = loader.get_template('create/bill_of_sale.html')
    context = {}

    return HttpResponse(template.render(context, request))