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

class AccountReceivable(models.Model):
    invoice_date = models.DateField()
    invoice_number = models.CharField(max_length=10)
    customer_name = models.CharField(max_length=100)
    total_amount = models.DecimalField(max_digits=15, decimal_places=2)
    due_date = models.DateField()
    balance = models.DecimalField(max_digits=15, decimal_places=2)
    service_type = models.CharField(max_length=50)
    percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  #percentage as a decimal then we will get the % from FrontEnd
    class Meta:
        verbose_name = "Account Receivable"
        verbose_name_plural = "Accounts Receivable"

    def __str__(self):
        return f"Invoice {self.invoice_number} - {self.customer_name}"

