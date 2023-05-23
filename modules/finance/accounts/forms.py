from django.forms import ModelForm

from .models import Analitic, Sintetic, TypeAccount


class AnaliticForm(ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(AnaliticForm, self).__init__(*args, **kwargs)
        self.fields['sintetic'].queryset = Sintetic.objects.filter(
            company=user.company).order_by('typeaccount__typeaccount', 'sintetic')

    class Meta:
        model = Analitic
        fields = ['sintetic', 'analitic']


class SinteticForm(ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(SinteticForm, self).__init__(*args, **kwargs)
        self.fields['typeaccount'].queryset = TypeAccount.objects.filter(
            company=user.company).order_by('typeaccount')

    class Meta:
        model = Sintetic
        fields = ['typeaccount', 'sintetic']
