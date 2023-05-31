from django import forms
from django.forms import (DateInput, NumberInput, Select, TextInput,
                          inlineformset_factory)

from modules.finance.accounts.models import Analitic

from .models import Document_Type, Entry, EntryItem


class DateInputAuto(DateInput):
    input_type = 'date'


class Document_Type_Form(forms.ModelForm):
    class Meta:
        model = Document_Type
        fields = ['document_type']


class Entry_Form(forms.ModelForm):

    def __init__(self, user, *args, **kwargs):
        super(Entry_Form, self).__init__(*args, **kwargs)
        self.fields['document_type'].queryset = Document_Type.objects.filter(
            company=user.company)
        # self.fields['credit'].label = 'value_ref'
        # self.fields['credit'].widget = 'value_ref'
        # self.fields['debit'].label = 'value_ref'
        # self.fields['debit'].widget = 'value_ref'

    class Meta:
        model = Entry
        fields = ['date', 'document_type', 'n_doc',
                  'total_value', 'description', 'obs', 'credit', 'debit']
        widgets = {
            'date': DateInput(attrs={
                'class': "form-control",
                'style': 'max-width: 200px;',
            }),
            'document_type': Select(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Tipo de Documento'
            }),
            'n_doc': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Núm. do Documento'
            }),
            'total_value': NumberInput(attrs={
                'class': "form-control clSum",
                'style': 'max-width: 200px;',
                'placeholder': 'Vr. do Documento'
            }),
            'description': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 560px;',
                'placeholder': 'Descrição do Documento'
            }),
            'obs': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 600px;',
                'placeholder': 'Observações'
            }),
            'credit': NumberInput(attrs={
                'id': "credit",
                'class': "form-control",
                'style': 'max-width: 200px;',
                'placeholder': 'Credito',
                'readonly': True
            }),
            'debit': NumberInput(attrs={
                'id': "debit",
                'class': "form-control",
                'style': 'max-width: 200px;',
                'placeholder': 'Debito',
                'readonly': True
            }),
        }


class EntryItem_Form(forms.ModelForm):

    class Meta:
        model = EntryItem
        fields = ['typemovement', 'account', 'value', 'value_ref']

        widgets = {
            'typemovement': Select(attrs={
                'class': "clSum",
                'style': 'max-width: 300px;',
            }),
            'value': NumberInput(attrs={
                'class': "clSum",
                'style': 'max-width: 200px;',
                'placeholder': 'Valor'
            }),
            'value_ref': NumberInput(attrs={
                'readonly': True
            }),
        }

    def __init__(self, *args, user, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)
        self.fields['account'].queryset = Analitic.objects.filter(
            company=self.user.company).order_by(
            'sintetic__typeaccount__typeaccount',
            'sintetic__sintetic',
            'analitic')
        self.fields['value_ref'].label = ""
        self.fields['value_ref'].widget = forms.HiddenInput()
        self.fields['typemovement'].label = "Type"
        self.fields['account'].label = "Account"
        self.fields['value'].label = "Value"
