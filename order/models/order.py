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
    user_note = models.CharField(max_length=50, null=True, blank=True)

    # destination address
    customer_name = models.CharField(max_length=20)
    customer_contact = models.CharField(max_length=13)
    base_address = models.CharField(max_length=255)
    detail_address = models.CharField(max_length=50, null=True, blank=True)
    postal_code = models.CharField(max_length=6)
    delivery_note = models.CharField(max_length=50, null=True, blank=True)

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
        product_name = self._get_product_name()
        return f"#{self.id} {self.alloff_order_id} - ({product_name})"

    def _get_product_name(self):
        try:
            count = self.order_items.count()
            first_product = self.order_items.first()
            product_name = first_product.product_name
            if count > 1:
                product_name += f" and {count - 1} more"
            return product_name
        except:
            return None

    @property
    def order_items(self):
        from .order_item import OrderItem

        return OrderItem.objects.filter(order__id=self.id)
