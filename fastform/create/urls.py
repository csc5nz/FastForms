# create urls

from django.urls import path

from . import views

app_name = 'create'
urlpatterns = [
    path('bill_of_sale', views.bill_of_sale, name='bill_of_sale'),
    path('view_bill_of_sale', views.view_bill_of_sale, name='view_bill_of_sale'),
]