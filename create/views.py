from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.template import loader
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.utils import timezone

from .models import BillOfSale
from .forms import BillOfSaleForm, BillOfSaleForm01

# Create your views here.

def create_bill_of_sale(request):
    template = loader.get_template('create/build_bill_of_sale_01.html')
    context = {}

    return HttpResponse(template.render(context, request))

def create_bill_of_sale_01(request):
    print('hello')
    if request.method == "POST":
        form = BillOfSaleForm01(request.POST)
        print(form.errors)
        if form.is_valid():
            print('form is valid')
            new_bill_of_sale = form.save()  
        else:
            print('not valid')
        return redirect('index:home')
    else:
        form = BillOfSaleForm01()
        print('get, form')
        print(form)
    return render(request, 'create/build_bill_of_sale_01.html', {'form': form, 'page': '01'})

@xframe_options_sameorigin
def view_bill_of_sale(request):
    template = loader.get_template('create/bill_of_sale.html')
    context = {}

    return HttpResponse(template.render(context, request))