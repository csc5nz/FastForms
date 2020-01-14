from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1>Create and Edit Documents</h1><p>Create a Document</p><p>Upload a PDF</p><p>Login</p>")
