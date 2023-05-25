from django.db import models
from django.urls import reverse, reverse_lazy

from modules.core.models import TimeStampedModel
from modules.finance.accounts.models import Analitic
from users.models import Company, User

TYPEMOVEMENT = (
    ('d', 'debito'),
    ('c', 'credito'),
)


class Document_Type(models.Model):
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    document_type = models.CharField(max_length=100)

    class Meta:
        ordering = ('document_type',)

    def __str__(self):
        return self.document_type

    def get_absolute_url(self):
        return reverse_lazy('entrys:document_type_detail', kwargs={'pk': self.pk})


class Entry(TimeStampedModel):
    employee = models.ForeignKey(User, on_delete=models.PROTECT)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    date = models.DateField()
    document_type = models.ForeignKey(Document_Type, on_delete=models.PROTECT)
    n_doc = models.CharField(max_length=10, blank=True, null=True)
    total_value = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.CharField(max_length=100, blank=True, null=True)
    obs = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse('finance-update', kwargs={'pk': self.pk})

    def __str__(self):
        return '{} - {} - {}'.format(self.date, self.description, self.total_value)


class EntryItem(models.Model):
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
    account = models.ForeignKey(Analitic, on_delete=models.PROTECT)
    typemovement = models.CharField(max_length=1, choices=TYPEMOVEMENT)
    value = models.DecimalField(max_digits=15, decimal_places=2)
    Validation = models.DecimalField(max_digits=15, decimal_places=2)

    class Meta:
        ordering = ('pk',)

    def __str__(self):
        return '{} - {} - {} - {} - {}'.format(self.pk, self.entry, self.typemovement, self.account, self.value)
