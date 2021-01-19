# create urls

from django.urls import path

from . import views

app_name = 'create'
urlpatterns = [
    path('', views.home, name='home'),
    path('create_bill_of_sale/', views.create_bill_of_sale, name='create_bill_of_sale'),
    path('create_bill_of_sale/<int:page>/', views.create_bill_of_sale, name='create_bill_of_sale'),
    path('create_bill_of_sale/<int:page>/<int:id>/', views.create_bill_of_sale, name='create_bill_of_sale'),
    path('create_bill_of_sale_01/', views.create_bill_of_sale_01, name='create_bill_of_sale_01'),
    path('create_bill_of_sale_01/<int:id>/', views.create_bill_of_sale_01, name='create_bill_of_sale_01'),
    path('create_bill_of_sale_02/<int:id>/', views.create_bill_of_sale_02, name='create_bill_of_sale_02'),
    path('create_bill_of_sale_03/<int:id>/', views.create_bill_of_sale_03, name='create_bill_of_sale_03'),
    path('view_bill_of_sale', views.view_bill_of_sale, name='view_bill_of_sale'),
    
]