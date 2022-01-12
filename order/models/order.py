from django.db import models


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


class Order(models.Model):
    alloff_order_id = models.CharField(max_length=100)
    order_status = models.CharField(
        max_length=50,
        choices=OrderStatus.choices,
    )

    # user
    user = models.JSONField()
    user_note = models.CharField(max_length=50)

    # price
    product_price = models.IntegerField()
    delivery_price = models.IntegerField()
    total_price = models.IntegerField()

    # timestamp
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    ordered_at = models.DateTimeField(null=True, blank=True)
    delivery_started_at = models.DateTimeField(null=True, blank=True)
    delivery_finished_at = models.DateTimeField(null=True, blank=True)
    cancel_requested_at = models.DateTimeField(null=True, blank=True)
    cancel_finished_at = models.DateTimeField(null=True, blank=True)
    confirmed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"#{self.id} {self.alloff_order_id}"

    @property
    def order_items(self):
        return "OrderItem".objects.filter(order__id=self.id)
