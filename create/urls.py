# create urls

from django.urls import path

from . import views

app_name = 'create'
urlpatterns = [
    path('bill_of_sale', views.bill_of_sale, name='bill_of_sale'),
]