from django.db import models
from django.db.models.fields import BooleanField
from django.db.models.fields.related import ForeignKey
from django.contrib.postgres.fields import ArrayField
from .order import Order, OrderType, OrderStatus
from logistics.models import Courier


class OrderItem(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.DO_NOTHING)
    order_item_code = models.CharField(max_length=50)  # (구)사서함 코드
    alloff_product_id = models.CharField(max_length=50)
    product_image = models.URLField()
    product_name = models.CharField(max_length=50)
    brand_key_name = models.CharField(max_length=50)
    brand_kor_name = models.CharField(max_length=50)
    removed = BooleanField(default=False)
    sales_price = models.IntegerField()
    size_description = ArrayField(
        ArrayField(models.CharField(max_length=255, blank=False))
    )
    cancel_description = ArrayField(
        ArrayField(models.CharField(max_length=255, blank=False))
    )
    delivery_description = ArrayField(
        ArrayField(models.CharField(max_length=255, blank=False))
    )
    order_type = models.CharField(
        max_length=50,
        choices=OrderType.choices,
    )
    order_status = models.CharField(
        choices=OrderStatus.choices,
        max_length=50,
    )
    tracking_url = models.URLField()
    tracking_number = models.CharField(max_length=50, null=True, blank=True)
    tracking_courier = models.ForeignKey(
        Courier,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
    )
    size = models.CharField(max_length=50)
    quantity = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    ordered_at = models.DateTimeField(null=True, blank=True)
    delivery_started_at = models.DateTimeField(null=True, blank=True)
    delivery_finished_at = models.DateTimeField(null=True, blank=True)
    cancel_requested_at = models.DateTimeField(null=True, blank=True)
    cancel_finished_at = models.DateTimeField(null=True, blank=True)
    confirmed_at = models.DateTimeField(null=True, blank=True)
