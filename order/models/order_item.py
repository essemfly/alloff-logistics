from django.db import models
from django.contrib.postgres.fields import ArrayField

from logistics.models import Courier, ReceivedItem, ReceivedItemStatus

from .order import Order, OrderStatus


class OrderItemType(models.TextChoices):
    NORMAL_ORDER = "NORMAL_ORDER"
    TIMEDEAL_ORDER = "TIMEDEAL_ORDER"
    EXHIBITION_ORDER = "EXHIBITION_ORDER"
    UNKNOWN_ORDER = "UNKNOWN_ORDER"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING)
    order_item_code = models.CharField(max_length=50)  # (구)사서함 코드
    order_item_type = models.CharField(
        max_length=50,
        choices=OrderItemType.choices,
    )
    order_status = models.CharField(
        choices=OrderStatus.choices,
        max_length=50,
    )

    # brand
    brand_key_name = models.CharField(max_length=50)
    brand_kor_name = models.CharField(max_length=50)

    # product
    alloff_product_id = models.CharField(max_length=50)
    product_image_url = models.URLField()
    product_name = models.CharField(max_length=50)
    size_description = ArrayField(
        ArrayField(models.CharField(max_length=255, blank=False))
    )
    cancel_description = ArrayField(
        ArrayField(models.CharField(max_length=255, blank=False))
    )
    delivery_description = ArrayField(
        ArrayField(models.CharField(max_length=255, blank=False))
    )
    is_removed = models.BooleanField(default=False)

    sales_price = models.IntegerField()
    size = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    quantity = models.PositiveSmallIntegerField()

    # tracking
    tracking_url = models.URLField(null=True, blank=True)
    tracking_number = models.CharField(max_length=50, null=True, blank=True)
    tracking_courier = models.ForeignKey(
        Courier,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    ordered_at = models.DateTimeField(null=True, blank=True)
    delivery_started_at = models.DateTimeField(null=True, blank=True)
    delivery_finished_at = models.DateTimeField(null=True, blank=True)
    cancel_requested_at = models.DateTimeField(null=True, blank=True)
    cancel_finished_at = models.DateTimeField(null=True, blank=True)
    confirmed_at = models.DateTimeField(null=True, blank=True)

    @property
    def product_option(self):
        if self.color is not None:
            return f"{self.size}-{self.color}"
        return self.size

    def __str__(self):
        return f"#{self.id} [{self.brand_key_name}] {self.product_name} ({self.product_option})"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.create_received_item()

    def create_received_item(self):
        ReceivedItem.objects.create(
            code=self.order_item_code,
            status=ReceivedItemStatus.SOURCING_REQUIRED,
            product_brand_id=self.brand_key_name,
            product_brand_name=self.brand_key_name,
            product_id=self.alloff_product_id,
            product_name=self.product_name,
            product_size=self.size,
            product_color=self.color,
        )
