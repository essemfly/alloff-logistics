from django.db import models
from itertools import chain

from logistics.models.inventory import Inventory


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
        Inventory, on_delete=models.PROTECT, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    log = models.ManyToManyField(
        Log, related_name='received_items', null=True, blank=True,)

    def __str__(self):
        return f"#{self.id} {self.product_name} ({self.code})"

    def to_dict(instance):
        opts = instance._meta
        data = {}
        for f in chain(opts.concrete_fields, opts.private_fields):
            data[f.name] = f.value_from_object(instance)
        for f in opts.many_to_many:
            data[f.name] = [i.id for i in f.value_from_object(instance)]
        return data

    @property
    def product_code(self):
        return f"{self.product_brand}___{''.join(self.product_name.split())}___{''.join(self.product_option.split())}"

    @property
    def product_option(self):
        return f"{self.product_color}___{''.join(self.product_size.split())}"
