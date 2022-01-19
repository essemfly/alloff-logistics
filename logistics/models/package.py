from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.db import models
import uuid

from .common import Log
from .courier import Courier


class PackageStatus(models.TextChoices):
    # 일반 배송 관련
    DELIVERY_PREPARING = "DELIVERY_PREPARING"
    DELIVERY_STARTED = "DELIVERY_STARTED"
    DELIVERY_FINISHED = "DELIVERY_FINISHED"

    # 해외배송 관련
    OVERSEA_SHIPMENT_PREPARING = "OVERSEA_SHIPMENT_PREPARING"
    OVERSEA_SHIPMENT_STARTED = "OVERSEA_SHIPMENT_STARTED"

    # 취소 관련
    CANCEL_REQUESTED = "CANCEL_REQUESTED"
    CANCEL_PENDING = "CANCEL_PENDING"
    CANCEL_FINISHED = "CANCEL_FINISHED"


class PackageRemarkRecordType(models.TextChoices):
    CANCELED = "CANCELED"  # 취소
    PARTIALLY_CANCELED = "PARTIALLY_CANCELED"  # 부분취소
    PARTIALLY_SHIPMENT = "PARTIALLY_SHIPMENT"  # 분리 배송
    COMBINE_SHIPMENT = "COMBINE_SHIPMENT"  # 합배송


class Package(models.Model):

    key = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)

    status = models.CharField(
        max_length=50,
        choices=PackageStatus.choices,
    )
    related_order_item_ids = ArrayField(
        base_field=models.CharField(max_length=20), default=list
    )

    # destination address
    customer_name = models.CharField(max_length=20)
    customer_contact = models.CharField(max_length=13)
    base_address = models.CharField(max_length=255)
    detail_address = models.CharField(max_length=50, null=True, blank=True)
    postal_code = models.CharField(max_length=6)
    delivery_note = models.CharField(max_length=50, null=True, blank=True)

    # tracking info
    tracking_number = models.CharField(max_length=50, null=True, blank=True)
    tracking_courier = models.ForeignKey(
        Courier,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        product_name = self._get_product_name()
        return f"""{self.customer_name}'s {product_name}"""

    def _get_product_name(self):
        try:
            count = self.inventories.count()
            first_product = self.inventories.first()
            product_name = first_product.product_name
            if count > 1:
                product_name += f" and {count - 1} more"
            return product_name
        except:
            return None

    @property
    def remark_records(self):
        return self.remark_record

    @property
    def inventories(self):
        return self.inventory


# 특이사항은 필터링이 가능
class PackageRemarkRecord(models.Model):
    package = models.ForeignKey(
        Package, on_delete=models.CASCADE, related_name="remark_record"
    )
    record_type = models.CharField(
        max_length=50,
        choices=PackageRemarkRecordType.choices,
    )
    description = models.CharField(max_length=50)
    reference = models.CharField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)


class PackageLog(Log):
    package = models.ForeignKey(Package, on_delete=models.DO_NOTHING)
