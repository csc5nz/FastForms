# create urls

from django.urls import path

from . import views

app_name = 'create'
urlpatterns = [
    path('', views.home, name='home'),
    path('my_documents', views.my_documents, name='my_documents'),
    path('create_bill_of_sale/', views.create_bill_of_sale, name='create_bill_of_sale'),
    path('create_bill_of_sale/<int:page>/', views.create_bill_of_sale, name='create_bill_of_sale'),
    path('create_bill_of_sale/<int:page>/<int:id>/', views.create_bill_of_sale, name='create_bill_of_sale'),
    path('view_bill_of_sale/', views.view_bill_of_sale, name='view_bill_of_sale'),
    path('view_bill_of_sale/<int:id>/', views.view_bill_of_sale, name='view_bill_of_sale'),
    path('view_bill_of_sale_pdf/', views.view_bill_of_sale_pdf, name='view_bill_of_sale_pdf'),
    path('view_bill_of_sale_pdf/<int:id>/', views.view_bill_of_sale_pdf, name='view_bill_of_sale_pdf'),
]