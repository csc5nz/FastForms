from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader

# Create your views here.
def bill_of_sale(request):
    template = loader.get_template('create/build_bill_of_sale_01.html')
    context = {}

    return HttpResponse(template.render(context, request))