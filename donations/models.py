from django.db import models

# Create your models here.


# Create your models here.
class Donation(models.Model):
    uuid = models.UUIDField(primary_key=True, editable=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    email = models.EmailField()
    donor = models.CharField(max_length=255, blank=True, null=True)
    product_code = models.CharField(max_length=100, blank=True, null=True, default="EPAYTEST")
    service_charge = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    delivery_charge = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    tax_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"Donation {self.uuid} - {self.amount} by {self.email}"
