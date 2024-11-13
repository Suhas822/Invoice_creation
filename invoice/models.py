from django.db import models

# Create your models here.
from django.db import models

class Invoice(models.Model):
    invoice_number = models.CharField(max_length=50, unique=True)
    customer_name = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return f"{self.invoice_number} - {self.customer_name}"

class InvoiceDetail(models.Model):
    invoice = models.ForeignKey(Invoice, related_name='details', on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    line_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.description} - {self.line_total}"