from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView

from modules.finance.accounts.models import TypeAccount
from modules.finance.entrys.models import Document_Type

from .forms import SignUpForm
from .models import Company


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(request, email=user.email,
                                password=raw_password)
            if user is not None:
                login(request, user)
            else:
                print("user is not authenticated")
            return redirect('users:company')
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form})


class NewCompany(CreateView):
    model = Company
    fields = ('company_name', 'company_nickname')

    def form_valid(self, form):
        obj = form.save()
        user_new = self.request.user
        user_new.company = obj
        user_new.save()
        a = TypeAccount(company=obj, typeaccount='1. ATIVO')
        a.save()
        b = TypeAccount(company=obj, typeaccount='2. PASSIVO')
        b.save()
        c = TypeAccount(company=obj, typeaccount='3. RECEITAS')
        c.save()
        d = TypeAccount(company=obj, typeaccount='4. DESPESAS E CUSTOS')
        d.save()
        e = Document_Type(company=obj, document_type='Nota Fiscal')
        e.save()
        f = Document_Type(company=obj, document_type='Recibo')
        f.save()
        g = Document_Type(company=obj, document_type='Duplicata')
        g.save()
        h = Document_Type(company=obj, document_type='Boleto')
        h.save()
        return redirect('index')


class EditCompany(UpdateView):
    model = Company
    fields = ('company_name', 'company_nickname')

    def get_object(self):
        return self.request.user.company
