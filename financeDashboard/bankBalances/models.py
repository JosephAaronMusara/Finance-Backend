from django.db import models

class Currency(models.Model):
    currency_code = models.CharField(max_length=5, unique=True)
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.currency_code

class CurrentAsset(models.Model):
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=20, decimal_places=2)

class NetCurrentAsset(models.Model):
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    odsecurity_amount = models.DecimalField(max_digits=20, decimal_places=2)
    odusage_amount = models.DecimalField(max_digits=20, decimal_places=2)

class UnutilizedGrant(models.Model):
    donor = models.CharField(max_length=50)#from what I understood on what grants are pandaita research
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=20, decimal_places=2)

class Total(models.Model):#not sure if its necessary since we are going to do the calculations on the FrontEnd
    description = models.CharField(max_length=50)
    total_amount = models.DecimalField(max_digits=20, decimal_places=2)
