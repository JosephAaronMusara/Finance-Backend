from django.db import models

class Currency(models.Model):
    currency_code = models.CharField(max_length=5, unique=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.currency_code

class BankBalance(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=30)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    
    def __str__(self):
        return f"{self.name} under {self.type}"

    
class Expense(models.Model):
    description = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=20, decimal_places=2)

class AccountReceivable(models.Model):
    invoice_date = models.DateField()
    invoice_number = models.CharField(max_length=10)
    customer_name = models.CharField(max_length=100)
    total_amount = models.DecimalField(max_digits=15, decimal_places=2)
    due_date = models.DateField()
    balance = models.DecimalField(max_digits=15, decimal_places=2)
    service_type = models.CharField(max_length=50)

    def __str__(self):
        return f"Invoice {self.invoice_number} - {self.customer_name}"

