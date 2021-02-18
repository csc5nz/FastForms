# create urls

from django.urls import path

from . import views

app_name = 'create'
urlpatterns = [
    path('', views.home, name='home'),
    path('my_documents', views.my_documents, name='my_documents'),
    path('create_document/<int:id>/', views.create_document, name='create_document'),
    path('create_bill_of_sale/', views.create_bill_of_sale, name='create_bill_of_sale'),
    path('create_bill_of_sale/<int:page>/', views.create_bill_of_sale, name='create_bill_of_sale'),
    path('create_bill_of_sale/<int:page>/<int:id>/', views.create_bill_of_sale, name='create_bill_of_sale'),
    path('view_document/<int:id>/', views.view_document, name='view_document'),
    path('view_bill_of_sale/', views.view_bill_of_sale, name='view_bill_of_sale'),
    path('view_bill_of_sale/<int:id>/', views.view_bill_of_sale, name='view_bill_of_sale'),
    path('view_pdf_document/<int:id>/', views.view_pdf_document, name='view_pdf_document'),
    path('view_pdf_bill_of_sale/', views.view_pdf_bill_of_sale, name='view_pdf_bill_of_sale'),
    path('view_pdf_bill_of_sale/<int:id>/', views.view_pdf_bill_of_sale, name='view_pdf_bill_of_sale'),
    path('delete_document/<int:id>/', views.delete_document, name='delete_document'),
]