from django.db import models
from django.contrib.postgres.fields import JSONField

from logistics.models import ReceivedItem
from logistics.models.received_item import ReceivedItemStatus
from .orderitem import OrderItem


class OrderStatus(models.TextChoices):
    ORDER_CREATED = "ORDER_CREATED"
    ORDER_RECREATED = "ORDER_RECREATED"
    PAYMENT_PENDING = "PAYMENT_PENDING"
    PAYMENT_FINISHED = "PAYMENT_FINISHED"
    PRODUCT_PREPARING = "PRODUCT_PREPARING"
    DELIVERY_PREPARING = "DELIVERY_PREPARING"
    DELIVERY_STARTED = "DELIVERY_STARTED"
    DELIVERY_FINISHED = "DELIVERY_FINISHED"
    CONFIRM_PAYMENT = "CONFIRM_PAYMENT"
    CANCEL_REQUESTED = "CANCEL_REQUESTED"
    CANCEL_PENDING = "CANCEL_PENDING"
    CANCEL_FINISHED = "CANCEL_FINISHED"


class OrderType(models.TextChoices):
    NORMAL_ORDER = "NORMAL_ORDER"
    TIMEDEAL_ORDER = "TIMEDEAL_ORDER"
    EXHIBITION_ORDER = "EXHIBITION_ORDER"
    UNKNOWN_ORDER = "UNKNOWN_ORDER"


class Order(models.Model):
    alloff_order_id = models.CharField(max_length=100)
    user = JSONField()
    order_status = models.CharField(
        max_length=50,
        choices=OrderStatus.choices,
    )
    product_price = models.IntegerField()
    delivery_price = models.IntegerField()
    total_price = models.IntegerField()
    user_note = models.CharField(max_length=50)

    # timestamp
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    ordered_at = models.DateTimeField(null=True, blank=True)
    delivery_started_at = models.DateTimeField(null=True, blank=True)
    delivery_finished_at = models.DateTimeField(null=True, blank=True)
    cancel_requested_at = models.DateTimeField(null=True, blank=True)
    cancel_finished_at = models.DateTimeField(null=True, blank=True)
    confirmed_at = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.create_received_items()

    def create_received_items(self):
        [
            ReceivedItem.objects.create(
                # code=self.code, # todo: create sourcing code
                status=ReceivedItemStatus.SOURCING_REQUIRED,
                product_id=product.product_id,
                product_brand_id=product.brand_id,
                product_brand_name=product.brand_name,
                product_name=product.name,
                product_size=product.size,
                product_color=product.color,
            )
            for product in self.products.all()
        ]

    def __str__(self):
        return f"#{self.id} {self.customer_name}"

    @property
    def order_items(self):
        return OrderItem.objects.filter(order__id=self.id)
