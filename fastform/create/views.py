from django.shortcuts import render, redirect, get_object_or_404, Http404

from django.http import HttpResponse
from django.template import loader
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.utils import timezone

from .models import BillOfSale, Document
from .forms import BillOfSaleForm, BillOfSaleForm01, BillOfSaleForm02, BillOfSaleForm03

# Create your views here.
def home(request):
    return render(request, 'create/home.html', {})

def my_documents(request):
    if request.user.is_authenticated:
        user = request.user
    else:
        return redirect('create:log_in')

    documents = Document.objects.filter(user=user)
    return render(request, 'create/my_documents.html', {'documents': documents})

def create_document(request, id):
    document = get_object_or_404(Document, id=id)
    address = 'create:create_' + document.doc_type
    return redirect(address, page=1, id=document.doc_id)   

def create_bill_of_sale(request, page=None, id=None):
    instance = get_object_or_404(BillOfSale, id=id) if id else None
    next_page = 0
    if request.user.is_authenticated:
        user = request.user
    else:
        user = None
    if instance and instance.user != user:
        return redirect('create:my_documents')

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
            id = bill_of_sale.id   
            if not instance:
                bill_of_sale.user = user
                bill_of_sale.save()
            
        else:
            print('not valid')
            print(form.errors)
        if page == 3:
            if user:    
                return redirect('create:my_documents')
            else:
                return redirect('create:log_in', id=bill_of_sale.document.id)
            # return redirect('index:home')    
        return redirect('create:create_bill_of_sale', page=next_page, id=id)
    
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
    context = {'form': form, 'page': page, "id" : id, "title" : title[page]}
    return render(request, 'create/build_bill_of_sale_01.html', context)

def view_document(request, id):
    document = get_object_or_404(Document, id=id)
    address = 'create:view_' + document.doc_type
    return redirect(address, id=document.doc_id)   


@xframe_options_sameorigin
def view_bill_of_sale(request, id=None):
    bill_of_sale = get_object_or_404(BillOfSale, id = id) if id else None
    template = loader.get_template('create/bill_of_sale.html')
    context = {'bill_of_sale': bill_of_sale}

    return HttpResponse(template.render(context, request))


def view_pdf_document(request, id):
    document = get_object_or_404(Document, id=id)
    address = 'create:view_pdf_' + document.doc_type
    return redirect(address, id=document.doc_id)   


from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa

def view_pdf_bill_of_sale(request, id=None):
    bill_of_sale = get_object_or_404(BillOfSale, id = id) if id else 0
    template = loader.get_template('create/bill_of_sale_pdf.html')
    context = {'bill_of_sale': bill_of_sale}
    html = template.render(context, request)
    
    response = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), response)
    if not pdf.err:
        return HttpResponse(response.getvalue(), content_type='application/pdf')
    else:
        return HttpResponse("Error Rendering PDF", status=400)

document_models = {"bill_of_sale": BillOfSale}
def delete_document(request, id):
    document = get_object_or_404(Document, id=id)
    document_child = get_object_or_404(document_models[document.doc_type], id=document.doc_id)
    document_child.delete()
    document.delete()
    return redirect('create:my_documents')

