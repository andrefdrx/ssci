

from django.db import models
from django.utils import timezone
# Create your models here.


class Item(models.Model):
    item = models.CharField(max_length=200)

    def __str__(self):
        return self.item


class Udm(models.Model):
    udm = models.CharField(max_length=10)

    def __str__(self):
        return self.udm


class Produto(models.Model):
    nome = models.ForeignKey(Item, on_delete=models.CASCADE)
    unid = models.ForeignKey(Udm, on_delete=models.CASCADE)
    qtde = models.IntegerField()
    obse = models.CharField(max_length=255, blank=True, null=True)
    data = models.DateTimeField(default=timezone.now)


# Create your models here.
