from django.db import models


class SupplierType(models.TextChoices):
    MADAM = "MADAM"
    MALL = "MALL"
    OFFLINE = "OFFLINE"
    INVENTORY = "INVENTORY"


class Supplier(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=SupplierType.choices)
    bank_name = models.CharField(max_length=20)
    bank_account_holder = models.CharField(max_length=40)
    bank_account_number = models.CharField(max_length=40)
    biz_registration_id = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
