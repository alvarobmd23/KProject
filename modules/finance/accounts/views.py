from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView

from .forms import AnaliticForm, SinteticForm
from .models import Analitic, Sintetic


def accountsview(request):
    company_user = Sintetic.objects.filter(
        company=request.user.company).order_by('typeaccount', 'sintetic', 'analitic')
    queryset = company_user.values(
        'company', 'company__company_name', 'typeaccount__typeaccount', 'sintetic', 'id', 'analitic__analitic', 'analitic__id').distinct()
    return render(request, 'accounts/accounts.html', {'objects': queryset})


class Analitic_New(CreateView):

    model = Analitic
    form_class = AnaliticForm

    def get_form_kwargs(self):
        kwargs = super(Analitic_New, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def form_valid(self, form):
        analitic = form.save(commit=False)
        analitic.company = self.request.user.company
        analitic.save()
        messages.success(
            self.request, 'Conta Analítica adicionada com sucesso!', 'alert-success')
        return super(Analitic_New, self).form_valid(form)


class Analitic_Update(UpdateView):
    model = Analitic
    form_class = AnaliticForm

    def get_form_kwargs(self):
        kwargs = super(Analitic_Update, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def form_valid(self, form):
        messages.success(
            self.request, 'Conta Analítica modificada com sucesso!', 'alert-success')
        return super(Analitic_Update, self).form_valid(form)


class Analitic_Delete(DeleteView):
    model = Analitic
    success_url = reverse_lazy('accounts:accounts')

    def get_queryset(self):
        company_user = self.request.user.company
        return Analitic.objects.filter(company=company_user)


class Sintetic_New(CreateView):
    model = Sintetic
    form_class = SinteticForm

    def get_form_kwargs(self):
        kwargs = super(Sintetic_New, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def form_valid(self, form):
        sintetic = form.save(commit=False)
        sintetic.company = self.request.user.company
        sintetic.save()
        messages.success(
            self.request, 'Conta Sintética adicionada com sucesso!', 'alert-success')
        return super(Sintetic_New, self).form_valid(form)


class Sintetic_Update(UpdateView):
    model = Sintetic
    form_class = SinteticForm

    def get_form_kwargs(self):
        kwargs = super(Sintetic_Update, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def form_valid(self, form):
        messages.success(
            self.request, 'Conta Sintética modificada com sucesso!', 'alert-success')
        return super(Sintetic_Update, self).form_valid(form)


class Sintetic_Delete(DeleteView):
    model = Sintetic
    success_url = reverse_lazy('accounts:accounts')

    def get_queryset(self):
        company_user = self.request.user.company
        return Sintetic.objects.filter(company=company_user)
