from django.shortcuts import render, redirect, get_object_or_404, Http404

from django.http import HttpResponse
from django.template import loader
# from django.views.decorators.clickjacking import xframe_options_sameorigin
# from django.utils import timezone
from django.contrib.auth import authenticate, login, logout

# from .models import BillOfSale, Document
from .user_forms import SignUpForm, LogInForm


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('create:my_documents')
    else:
        form = SignUpForm()
        print(form)
    return render(request, 'create/sign_up.html', {'form': form})


def log_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('create:my_documents')
        else:
            return HttpResponse("Invalid login ingormation.")
    else:
        form = LogInForm()
    return render(request, 'create/log_in.html', {'form': form})