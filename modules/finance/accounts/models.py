from django.db import models
from django.urls import reverse

from users.models import Company


class TypeAccount(models.Model):
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    typeaccount = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse("accounts:accounts")

    def __str__(self):
        return self.typeaccount


class Sintetic(models.Model):
    typeaccount = models.ForeignKey(TypeAccount, on_delete=models.PROTECT)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    sintetic = models.CharField(max_length=100)

    @property
    def concatsintetic(self):
        return "%s / %s" % (self.typeaccount.typeaccount, self.sintetic)

    def get_absolute_url(self):
        return reverse("accounts:accounts")

    def __str__(self):
        return self.concatsintetic


class Analitic(models.Model):
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    sintetic = models.ForeignKey(Sintetic, on_delete=models.PROTECT)
    analitic = models.CharField(max_length=100)

    @property
    def concatanalitic(self):
        return "%s / %s" % (self.sintetic.concatsintetic, self.analitic)

    def get_absolute_url(self):
        return reverse("accounts:accounts")

    def __str__(self):
        return self.concatanalitic
