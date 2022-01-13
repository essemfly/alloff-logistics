from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.db import models
import uuid

from .courier import Courier
from .inventory import Inventory


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


# 특이사항은 필터링이 가능
class PackageRemarkRecord(models.Model):

    record_type = models.CharField(
        max_length=50,
        choices=PackageRemarkRecordType.choices,
    )
    description = models.CharField(max_length=50)
    reference = models.CharField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)


class Package(models.Model):

    key = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)

    status = models.CharField(
        max_length=50,
        choices=PackageStatus.choices,
    )
    remark_records = models.ForeignKey(
        PackageRemarkRecord,
        on_delete=models.CASCADE,
    )
    related_order_item_ids = ArrayField(
        base_field=models.CharField(max_length=20), default=list
    )
    inventories = models.ForeignKey(Inventory, on_delete=models.DO_NOTHING)

    # destination address
    customer_name = models.CharField(max_length=20)
    customer_contact = models.CharField(max_length=13)
    base_address = models.CharField(max_length=255)
    detail_address = models.CharField(max_length=50, null=True, blank=True)
    postal_code = models.CharField(max_length=6)
    delivery_note = models.CharField(max_length=50)

    # tracking info
    tracking_number = models.CharField(max_length=50)
    tracking_courier = models.ForeignKey(Courier, on_delete=models.DO_NOTHING)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
