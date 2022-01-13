from django.db import models


class PaymentStatus(models.TextChoices):
    PAYMENT_CREATED = "PAYMENT_CREATED"
    PAYMENT_CONFIRMED = "PAYMENT_CONFIRMED"
    PAYMENT_TIME_OUT = "PAYMENT_TIME_OUT"
    PAYMENT_CANCELED = "PAYMENT_CANCELED"
    PAYMENT_REFUND_REQUESTED = "PAYMENT_REFUND_REQUESTED"
    PAYMENT_REFUND_FINISHED = "PAYMENT_REFUND_FINISHED"


class Payment(models.Model):
    imp_uid = models.CharField(max_length=100)
    payment_status = models.CharField(
        max_length=50,
        choices=PaymentStatus.choices,
    )
    pg = models.CharField(max_length=20)
    pay_method = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    merchant_uid = models.CharField(max_length=100)
    amount = models.PositiveIntegerField()
    buyer_name = models.CharField(max_length=20)
    buyer_mobile = models.CharField(max_length=20)
    buyer_address = models.CharField(max_length=100)
    buyer_post_code = models.CharField(max_length=20)
    company = models.CharField(max_length=20)
    app_scheme = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"#{self.id} [{self.pg}] {self.imp_uid}"
