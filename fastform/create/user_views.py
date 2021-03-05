from django.shortcuts import render, redirect, get_object_or_404, Http404

from django.http import HttpResponse
from django.template import loader
# from django.views.decorators.clickjacking import xframe_options_sameorigin
# from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# from .models import BillOfSale, Document
from .user_forms import SignUpForm, LogInForm
from .models import Document, BillOfSale



def sign_up(request, id=None):
    document = get_object_or_404(Document, id=id) if id else None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            if document:
                document.user = user
                document.save()
                doc_child = get_object_or_404(document_models[document.doc_type], id=document.doc_id)
                doc_child.user = user
                doc_child.save()
            
            return redirect('create:my_documents')
    else:
        form = SignUpForm()
        print(form)
    return render(request, 'create/sign_up.html', {'form': form})


document_models = {"bill_of_sale": BillOfSale}
def log_in(request, id=None):
    document = get_object_or_404(Document, id=id) if id else None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if document:
                document.user = user
                document.save()
                doc_child = get_object_or_404(document_models[document.doc_type], id=document.doc_id)
                doc_child.user = user
                doc_child.save()
                
            return redirect('create:my_documents')
        else:
            return HttpResponse("Invalid login ingormation.")
    else:
        form = AuthenticationForm() #LogInForm()
    return render(request, 'create/log_in.html', {'form': form, 'document':document})


def log_out(request):
    logout(request)
    return redirect('create:home')