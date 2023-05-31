from django.contrib.auth.decorators import login_required
from django.urls import path

from .views import (Document_Type_Create, Document_Type_Delete,
                    Document_Type_Update, Entry_Delete, document_type_detail,
                    document_type_list, entrys_add, entrys_detail, entrys_edit,
                    entrys_list)

app_name = 'entrys'

urlpatterns = [
    # Document_Type
    path('document_type/',
         login_required(document_type_list), name='document_type'),
    path('document_type/<int:pk>/',
         login_required(document_type_detail), name='document_type_detail'),
    path('document_type/add/',
         login_required(Document_Type_Create.as_view()), name='document_type_add'),
    path('document_type/edit/<int:pk>/',
         login_required(Document_Type_Update.as_view()), name='document_type_edit'),
    path('document_type/delete/<int:pk>/',
         login_required(Document_Type_Delete.as_view()), name='document_type_delete'),

    # Entrys
    path('entrys/',
         login_required(entrys_list), name='entrys'),
    path('entrys/<int:pk>/',
         login_required(entrys_detail), name='entrys_detail'),
    path('entrys/add/',
         login_required(entrys_add), name='entrys_add'),
    path('entrys/edit/<int:pk>/',
         login_required(entrys_edit), name='entrys_edit'),
    path('entrys/delete/<int:pk>/',
         login_required(Entry_Delete.as_view()), name='entrys_delete'),


]
