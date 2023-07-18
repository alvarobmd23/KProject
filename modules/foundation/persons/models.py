from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse

from modules.core.models import TimeStampedModel
from users.models import Company, User

TYPEPERSON = (
    ('pf', 'pessoa fisica'),
    ('pj', 'pessoa juridica'),
)

TYPECONTACT = (
    ('c', 'celular'),
    ('e', 'e-mail'),
    ('t', 'telefone'),
)

PERCENTAGE_VALIDATOR = [MinValueValidator(0), MaxValueValidator(100)]


class Person(TimeStampedModel):
    employee = models.ForeignKey(User, on_delete=models.PROTECT)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    typeperson = models.CharField(max_length=2, choices=TYPEPERSON)
    name = models.CharField(max_length=60)
    nickname = models.CharField(max_length=60, blank=True, null=True)
    cpf_cnpj = models.CharField(max_length=20, blank=True, null=True)
    rg_ie = models.CharField(max_length=20, blank=True, null=True)
    anniversary_fundationdate = models.DateField(blank=True, null=True)
    cep = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=60, blank=True, null=True)
    city = models.CharField(max_length=20, blank=True, null=True)
    uf = models.CharField(max_length=2, blank=True, null=True)
    country = models.CharField(max_length=20, blank=True, null=True)
    obs = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return '{} - {} {}'.format(
            self.name, self.typeperson, self.cpf_cnpj)

    def get_absolute_url(self):
        return reverse("persons:persons")

    def date_formated(self):
        return self.anniversary_fundationdate.strftime('%d/%m/%Y')


class PersonContact(models.Model):
    person = models.ForeignKey(
        Person, on_delete=models.CASCADE)
    typecontact = models.CharField(max_length=1, choices=TYPECONTACT)
    contactdescription = models.CharField(max_length=60, blank=True, null=True)
    contactobs = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        ordering = ('pk',)

    def __str__(self):
        return '{} - {} - {} - {}'.format(
            self.pk, self.person, self.typecontact, self.contactdescription)


class PersonSeller(models.Model):
    person = models.ForeignKey(
        Person, on_delete=models.CASCADE)
    commission = models.DecimalField(
        max_digits=3, decimal_places=0,
        default=0, validators=PERCENTAGE_VALIDATOR)
    sellerobs = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        ordering = ('pk',)

    def __str__(self):
        return '{} - {} - {}'.format(
            self.pk, self.person, self.commission)


class PersonCustomer(models.Model):
    person = models.ForeignKey(
        Person, on_delete=models.CASCADE)
    fin_discount = models.DecimalField(
        max_digits=3, decimal_places=0,
        default=0, validators=PERCENTAGE_VALIDATOR)
    payment_term = models.DecimalField(max_digits=3, decimal_places=0)
    customerobs = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        ordering = ('pk',)

    def __str__(self):
        return '{} - {} - {}'.format(
            self.pk, self.person, self.commission)
