from django.contrib import messages
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, resolve_url
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView

from modules.finance.accounts.models import Analitic

from .forms import Document_Type_Form, Entry_Form, EntryItem_Form
from .models import Person, PersonContact, PersonCustomer, PersonSeller

# Persons


def entrys_list(request):
    template_name = 'entrys/entry_list.html'
    objects = Entry.objects.all().filter(company=request.user.company)
    context = {'object_list': objects}
    return render(request, template_name, context)


def entrys_detail(request, pk):

    template_name = 'entrys/entry_detail.html'
    obj = Entry.objects.filter(company=request.user.company).get(pk=pk)
    context = {'object': obj}
    return render(request, template_name, context)


def entrys_add(request):
    template_name = 'entrys/entry_form.html'
    entry_form = Entry()
    item_entry_formset = inlineformset_factory(
        Entry,
        EntryItem,
        form=EntryItem_Form,
        extra=0,
        min_num=1,
        validate_min=True,
    )
    if request.method == 'POST':
        form = Entry_Form(
            request.user,
            request.POST,
            instance=entry_form,
            prefix='main')
        formset = item_entry_formset(
            request.POST,
            instance=entry_form,
            prefix='entry',
            form_kwargs={'user': request.user}
        )
        if form.is_valid() and formset.is_valid():
            form = form.save(commit=False)
            if form.credit == form.debit == form.total_value:
                form.employee = request.user
                form.company = request.user.company
                form = form.save()
                formset = formset.save()
                messages.success(request,
                                 'Lançamento efetuado com sucesso!',
                                 'alert-success')
                return HttpResponseRedirect(reverse_lazy('entrys:entrys_add'))
            else:
                if form.credit != form.debit:
                    messages.warning(request,
                                     'Diferença entre Valores de Crédito e Débito no Accounts',
                                     'alert-warning')
                else:
                    messages.warning(request,
                                     'Conferir Valor Total com Valores do Accounts',
                                     'alert-warning')
                form = Entry_Form(
                    request.user,
                    instance=entry_form,
                    prefix='main')
    else:
        form = Entry_Form(
            request.user,
            instance=entry_form,
            prefix='main')
        formset = item_entry_formset(
            instance=entry_form,
            prefix='entry',
            form_kwargs={'user': request.user})

    context = {'form': form, 'formset': formset}
    return render(request, template_name, context)


def entrys_edit(request, pk):
    template_name = 'entrys/entry_form.html'
    entry_form = Entry.objects.filter(company=request.user.company).get(pk=pk)
    item_entry_formset = inlineformset_factory(
        Entry,
        EntryItem,
        form=EntryItem_Form,
        extra=0,
        min_num=1,
        validate_min=True,
    )
    if request.method == 'POST':
        form = Entry_Form(
            request.user,
            request.POST,
            instance=entry_form,
            prefix='main')
        formset = item_entry_formset(
            request.POST,
            instance=entry_form,
            prefix='entry',
            form_kwargs={'user': request.user}
        )
        if form.is_valid() and formset.is_valid():
            form = form.save(commit=False)
            if form.credit == form.debit == form.total_value:
                form.employee = request.user
                form.company = request.user.company
                form = form.save()
                formset = formset.save()
                messages.success(request,
                                 'Lançamento alterado com sucesso!',
                                 'alert-success')
                return HttpResponseRedirect(reverse_lazy('entrys:entrys'))
            else:
                if form.credit != form.debit:
                    messages.warning(request,
                                     'Diferença entre Valores de Crédito e Débito no Accounts!',
                                     'alert-warning')
                else:
                    messages.warning(request,
                                     'Conferir Valor Total com Valores do Accounts!',
                                     'alert-warning')
                form = Entry_Form(
                    request.user,
                    instance=entry_form,
                    prefix='main')
                formset = item_entry_formset(
                    instance=entry_form,
                    prefix='entry',
                    form_kwargs={'user': request.user})
    else:
        form = Entry_Form(
            request.user,
            instance=entry_form,
            prefix='main')
        formset = item_entry_formset(
            instance=entry_form,
            prefix='entry',
            form_kwargs={'user': request.user})

    context = {'form': form, 'formset': formset}
    return render(request, template_name, context)


class Entry_Delete(DeleteView):
    model = Entry
    success_url = reverse_lazy('entrys:entrys')

    def get_queryset(self):
        company_user = self.request.user.company
        return Entry.objects.filter(company=company_user)
