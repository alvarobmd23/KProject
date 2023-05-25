from django import forms

from .models import Document_Type


class Document_Type_Form(forms.ModelForm):

    class Meta:
        model = Document_Type
        fields = ['document_type']
