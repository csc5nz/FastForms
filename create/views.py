from django.shortcuts import render, redirect, get_object_or_404, Http404

from django.http import HttpResponse
from django.template import loader
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.utils import timezone

from .models import BillOfSale
from .forms import BillOfSaleForm, BillOfSaleForm01, BillOfSaleForm02, BillOfSaleForm03

# Create your views here.
def home(request):
    return render(request, 'create/home.html', {})


def create_bill_of_sale(request, page=None, id=None):
    instance = get_object_or_404(BillOfSale, id=id) if id else BillOfSale.objects.create()
    next_page = 0
    if request.method == "POST":
        if page is None or page == 1:
            page = 1
            form = BillOfSaleForm01(request.POST, instance=instance)
            next_page = 2
        elif page == 2 and id:
            form = BillOfSaleForm02(request.POST, instance=instance)
            next_page = 3
        elif page == 3 and id:
            form = BillOfSaleForm03(request.POST, instance=instance)
        else:
            print("****PAGE ", page)
            raise Http404("Page does not exist")

        if form.is_valid():
            bill_of_sale = form.save()  
        else:
            print('not valid')
        if page == 3:    
            return redirect('create:view_bill_of_sale', id=instance.id)    
            # return redirect('index:home')    
        return redirect('create:create_bill_of_sale', page=next_page, id=instance.id)
    
    else:
        title = {1: "Who is the Seller?", 2: "Who is the Buyer?", 3: "What is the Property?"}
        if page is None or page == 1:
            page = 1
            form = BillOfSaleForm01(instance=instance)
        elif page == 2 and id:
            form = BillOfSaleForm02(instance=instance)
        elif page == 3 and id:
            form = BillOfSaleForm03(instance=instance)
        else:
            raise Http404("Page does not exist")
    context = {'form': form, 'page': page, "id" : instance.id, "title" : title[page]}
    return render(request, 'create/build_bill_of_sale_01.html', context)


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
def view_bill_of_sale(request, id):
    bill_of_sale = get_object_or_404(BillOfSale, id = id)
    template = loader.get_template('create/bill_of_sale.html')
    context = {'bill_of_sale': bill_of_sale}

    return HttpResponse(template.render(context, request))




from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa

def view_pdf(request, id):
    bill_of_sale = get_object_or_404(BillOfSale, id = id)
    template = loader.get_template('create/bill_of_sale_pdf.html')
    context = {'bill_of_sale': bill_of_sale}
    html = template.render(context, request)
    
    response = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), response)
    if not pdf.err:
        return HttpResponse(response.getvalue(), content_type='application/pdf')
    else:
        return HttpResponse("Error Rendering PDF", status=400)
