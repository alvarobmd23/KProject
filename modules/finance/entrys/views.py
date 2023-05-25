from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import Document_Type_Form
from .models import Document_Type, Entry, EntryItem


def document_type_list(request):
    template_name = 'document_type/document_type_list.html'
    objects = Document_Type.objects.all().filter(company=request.user.company)
    context = {'object_list': objects}
    return render(request, template_name, context)


def document_type_detail(request, pk):
    template_name = 'document_type/document_type_detail.html'
    obj = Document_Type.objects.filter(company=request.user.company).get(pk=pk)
    context = {'object': obj}
    return render(request, template_name, context)


class Document_Type_Create(CreateView):
    model = Document_Type
    template_name = 'document_type/document_type_form.html'
    form_class = Document_Type_Form
    success_url = reverse_lazy('entrys:document_type')

    def form_valid(self, form):
        document_type = form.save(commit=False)
        document_type.company = self.request.user.company
        document_type.save()
        messages.success(
            self.request, 'Tipo de Documento adicionado com sucesso!', 'alert-success')
        return super(Document_Type_Create, self).form_valid(form)


class Document_Type_Update(UpdateView):
    model = Document_Type
    template_name = 'document_type/document_type_form.html'
    form_class = Document_Type_Form
    success_url = reverse_lazy('entrys:document_type')

    def get_queryset(self):
        company_user = self.request.user.company
        return Document_Type.objects.filter(company=company_user)

    def form_valid(self, form):
        messages.success(
            self.request, 'Tipo de Documento modificado com sucesso!', 'alert-success')
        return super(Document_Type_Update, self).form_valid(form)


class Document_Type_Delete(DeleteView):
    model = Document_Type
    template_name = 'document_type/document_type_delete.html'
    success_url = reverse_lazy('entrys:document_type')

    def get_queryset(self):
        company_user = self.request.user.company
        return Document_Type.objects.filter(company=company_user)
