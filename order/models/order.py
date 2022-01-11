from django.db import models

from logistics.models import Courier, ReceivedItem
from logistics.models.received_item import ReceivedItemStatus
from order.models.common import Product


class OrderStatus(models.TextChoices):
    PAYMENT_FINISHED = "PAYMENT_FINISHED"
    PRODUCT_PREPARING = "PRODUCT_PREPARING"
    DELIVERY_PREPARING = "DELIVERY_PREPARING"
    DELIVERY_STARTED = "DELIVERY_STARTED"
    DELIVERY_FINISHED = "DELIVERY_FINISHED"
    CONFIRM_PAYMENT = "CONFIRM_PAYMENT"
    CANCEL_REQUESTED = "CANCEL_REQUESTED"
    CANCEL_PENDING = "CANCEL_PENDING"
    CANCEL_FINISHED = "CANCEL_FINISHED"


class Order(models.Model):

    order_status = models.CharField(
        max_length=50,
        choices=OrderStatus.choices,
    )

    # user info
    user_id = models.CharField(max_length=20)

    # destination address
    customer_name = models.CharField(max_length=20)
    customer_contact = models.CharField(max_length=13)
    base_address = models.CharField(max_length=255)
    detail_address = models.CharField(max_length=50, null=True, blank=True)
    postal_code = models.CharField(max_length=6)
    delivery_note = models.CharField(max_length=50)

    # payment info
    transaction_id = models.CharField(max_length=255)
    product_price = models.IntegerField()
    delivery_price = models.IntegerField()
    total_price = models.IntegerField()

    products = models.ManyToManyField(Product, blank=True)

    # tracking info
    tracking_number = models.CharField(max_length=50, null=True, blank=True)
    tracking_courier = models.ForeignKey(
        Courier,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
    )

    # status
    confirmed_at = models.DateTimeField(null=True, blank=True)
    cancel_requested_at = models.DateTimeField(null=True, blank=True)
    cancel_confirmed_at = models.DateTimeField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

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


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    quantity = models.PositiveSmallIntegerField()
    received_item = models.ForeignKey(ReceivedItem, on_delete=models.DO_NOTHING)
