from django.db import models


class InventoryStatus(models.TextChoices):
    IN_STOCK = "IN_STOCK"
    PROCESSING_NEEDED = "PROCESSING_NEEDED"
    SHIPPED = "SHIPPED"
    SHIPPING_PENDING = "SHIPPING_PENDING"


class Inventory(models.Model):

    code = models.CharField(max_length=30, db_index=True)
    status = models.CharField(max_length=30, choices=InventoryStatus.choices)

    # product
    product_id = models.CharField(max_length=50)
    product_brand_name = models.CharField(max_length=20)
    product_name = models.CharField(max_length=20)
    product_size = models.CharField(max_length=50)

    location = models.CharField(max_length=50, null=False, blank=True)
    memo = models.TextField(null=False, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'inventories'

    def __str__(self):
        return f"Inventory #{self.id} [{self.status}] {self.product_name} ({self.code})"

    @property
    def product_code(self):
        return f"{self.product_brand_name}___{''.join(self.product_name.split())}___{''.join(self.product_size.split())}"
