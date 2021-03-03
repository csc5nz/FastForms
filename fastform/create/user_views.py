from django.shortcuts import render, redirect, get_object_or_404, Http404

from django.http import HttpResponse
from django.template import loader
# from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.utils import timezone

# from .models import BillOfSale, Document
# from .forms import BillOfSaleForm, BillOfSaleForm01, BillOfSaleForm02, BillOfSaleForm03


def sign_up(request):
    return render(request, 'create/sign_up.html', {})


def log_in(request):
    return render(request, 'create/log_in.html', {})