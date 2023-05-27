from django import forms

from modules.finance.accounts.models import Analitic

from .models import Document_Type, Entry, EntryItem


class Document_Type_Form(forms.ModelForm):
    class Meta:
        model = Document_Type
        fields = ['document_type']


class Entry_Form(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(format='%d/%m/%Y'),
        input_formats=['%d/%m/%Y']
    )

    def __init__(self, user, *args, **kwargs):
        super(Entry_Form, self).__init__(*args, **kwargs)
        self.fields['document_type'].queryset = Document_Type.objects.filter(
            company=user.company)

    class Meta:
        model = Entry
        fields = ['date', 'document_type', 'n_doc',
                  'total_value', 'description', 'obs']


class EntryItem_Form(forms.ModelForm):

    def __init__(self, *args, user, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)
        self.fields['account'].queryset = Analitic.objects.filter(
            company=self.user.company)

    class Meta:
        model = EntryItem
        fields = ['typemovement', 'account', 'value']
