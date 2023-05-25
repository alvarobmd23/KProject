from django.contrib.auth.decorators import login_required
from django.urls import path

from .views import (Document_Type_Create, Document_Type_Delete,
                    Document_Type_Update, document_type_detail,
                    document_type_list)

app_name = 'entrys'

urlpatterns = [
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
]
