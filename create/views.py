from django.shortcuts import render, redirect, get_object_or_404

from django.http import HttpResponse
from django.template import loader
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.utils import timezone

from .models import BillOfSale
from .forms import BillOfSaleForm, BillOfSaleForm01, BillOfSaleForm02, BillOfSaleForm03

# Create your views here.

def create_bill_of_sale(request, page, id=None):
    instance = get_object_or_404(BillOfSale, id=id) if id else None
    next_page = 0
    if request.method == "POST":
        if page == 1:
            form = BillOfSaleForm01(request.POST, instance=instance)
            next_page = 2
        elif page == 2 and id:
            form = BillOfSaleForm02(request.POST, instance=instance)
            next_page = 3
        elif page == 3 and id:
            form = BillOfSaleForm03(request.POST, instance=instance)
        else:
            raise Http404("Page does not exist")

        if form.is_valid():
            bill_of_sale = form.save()  
        else:
            print('not valid')
        if page == 3:    
            return redirect('index:home')    
        return redirect('create:create_bill_of_sale', page=next_page, id=bill_of_sale.id)
    
    else:
        if page == 1:
            form = BillOfSaleForm01(instance=instance)
        elif page == 2 and id:
            form = BillOfSaleForm02(instance=instance)
        elif page == 3 and id:
            form = BillOfSaleForm03(instance=instance)
        else:
            raise Http404("Page does not exist")

    return render(request, 'create/build_bill_of_sale_01.html', {'form': form, 'page': '01'})


def create_bill_of_sale_01(request, id=None):
    instance = get_object_or_404(BillOfSale, id=id) if id else None
    if request.method == "POST":
        form = BillOfSaleForm01(request.POST, instance=instance)
        if form.is_valid():
            bill_of_sale = form.save()  
        else:
            print('not valid')
        return redirect('create:create_bill_of_sale_02', id=bill_of_sale.id)
    else:
        form = BillOfSaleForm01(instance=instance)
    return render(request, 'create/build_bill_of_sale_01.html', {'form': form, 'page': '01'})

def create_bill_of_sale_02(request, id=None):
    instance = get_object_or_404(BillOfSale, id=id)
    if request.method == "POST":
        form = BillOfSaleForm02(request.POST, instance=instance)
        if form.is_valid():
            bill_of_sale = form.save()  
        else:
            print('not valid')
        return redirect('create:create_bill_of_sale_03', id=bill_of_sale.id)
    else:
        form = BillOfSaleForm02(instance=instance)
    return render(request, 'create/build_bill_of_sale_01.html', {'form': form, 'page': '01'})

def create_bill_of_sale_03(request, id=None):
    instance = get_object_or_404(BillOfSale, id=id)
    if request.method == "POST":
        form = BillOfSaleForm03(request.POST, instance=instance)
        if form.is_valid():
            bill_of_sale = form.save()  
        else:
            print('not valid')
        return redirect('index:home')
    else:
        form = BillOfSaleForm03(instance=instance)
    return render(request, 'create/build_bill_of_sale_01.html', {'form': form, 'page': '01'})

@xframe_options_sameorigin
def view_bill_of_sale(request):
    template = loader.get_template('create/bill_of_sale.html')
    context = {}

    return HttpResponse(template.render(context, request))