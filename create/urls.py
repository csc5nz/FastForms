# create urls

from django.urls import path

from . import views

app_name = 'create'
urlpatterns = [
    path('create_bill_of_sale', views.create_bill_of_sale, name='create_bill_of_sale'),
    path('create_bill_of_sale_01', views.create_bill_of_sale_01, name='create_bill_of_sale_01'),
    path('view_bill_of_sale', views.view_bill_of_sale, name='view_bill_of_sale'),
    
]