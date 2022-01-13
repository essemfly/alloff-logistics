from django.db import models
from logistics.models.inventory import Inventory, InventoryStatus
from .common import Log


class ReceivedItemStatus(models.TextChoices):
    SOURCING_REQUIRED = "SOURCING_REQUIRED"  # 발주 필요
    ON_RECEIVING = "ON_RECEIVING"  # 입고 중
    RECEIVED = "RECEIVED"  # 입고 완료
    OUT_OF_STOCK = "OUT_OF_STOCK"  # 취소됨 (재고부족)
    CANCELED = "CANCELED"  # 취소됨 (고객 취소)


class ReceivedItem(models.Model):

    code = models.CharField(max_length=30, db_index=True)
    status = models.CharField(
        max_length=50,
        choices=ReceivedItemStatus.choices,
        default=ReceivedItemStatus.SOURCING_REQUIRED,
    )

    # product
    product_id = models.CharField(max_length=20)
    product_name = models.CharField(max_length=20)
    product_brand_id = models.CharField(max_length=20)
    product_brand_name = models.CharField(max_length=20)
    product_size = models.CharField(max_length=10)
    product_color = models.CharField(max_length=10)

    # inventory
    inventory = models.ForeignKey(
        Inventory, on_delete=models.PROTECT, null=True, blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    # log = models.ManyToManyField(
    #     Log, related_name='received_items', null=True, blank=True,)

    def __str__(self):
        return f"#{self.id} {self.product_name} ({self.code})"

    def change_status(self, request, status):
        if status == self.status:  # same status
            return

        ReceivedItemLog.objects.create(
            received_item=self,
            description=f"change status {self.status} >> {status}",
            created_by=request.user,
        )
        self.status = status

        if status == ReceivedItemStatus.RECEIVED:
            self.inventory = self.create_inventory()

        self.save()

    def create_inventory(self):
        new_inventory = Inventory.objects.create(
            code=self.code,
            status=InventoryStatus.PROCESSING_NEEDED,
            product_id=self.product_id,
            product_brand_name=self.product_brand_name,
            product_name=self.product_name,
            product_size=self.product_size,
            product_color=self.product_color,
        )
        return new_inventory

    @property
    def product_code(self):
        return f"{self.product_brand}___{''.join(self.product_name.split())}___{''.join(self.product_option.split())}"

    @property
    def product_option(self):
        return f"{self.product_color}___{''.join(self.product_size.split())}"


class ReceivedItemLog(Log):
    received_item = models.ForeignKey(to=ReceivedItem, on_delete=models.DO_NOTHING)
