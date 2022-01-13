from django.db import models


from .common import Log


class InventoryStatus(models.TextChoices):
    CREATED = "CREATED"
    IN_STOCK = "IN_STOCK"
    PROCESSING_NEEDED = "PROCESSING_NEEDED"
    SHIPPED = "SHIPPED"
    SHIPPING_PENDING = "SHIPPING_PENDING"


class Inventory(models.Model):

    code = models.CharField(max_length=30, db_index=True)
    status = models.CharField(
        max_length=30, choices=InventoryStatus.choices, default=InventoryStatus.CREATED
    )

    # product
    product_id = models.CharField(max_length=20)
    product_name = models.CharField(max_length=20)
    product_brand_id = models.CharField(max_length=20)
    product_brand_name = models.CharField(max_length=20)
    product_size = models.CharField(max_length=10)
    product_color = models.CharField(max_length=10)

    location = models.CharField(max_length=50, null=False, blank=True)
    memo = models.TextField(null=False, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "inventories"

    def __str__(self):
        return f"#{self.id} {self.product_name} ({self.code})"

    def change_status(self, request, status):
        if status == self.status:  # same status
            return

        # create log
        InventoryLog.objects.create(
            inventory=self,
            description=f"change status {self.status} >> {status}",
            created_by=request.user,
            field_name="status",
            before=self.status,
            after=status,
        )
        self.status = status

        self.save()

    @property
    def product_code(self):
        return f"{self.product_brand_name}___{''.join(self.product_name.split())}___{''.join(self.product_size.split())}"


class InventoryLog(Log):
    inventory = models.ForeignKey(Inventory, on_delete=models.DO_NOTHING)
