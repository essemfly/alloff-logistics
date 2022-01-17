from datetime import date, datetime, timedelta
from django.db import models

from .inventory import Inventory


class ShippingNoticeStatus(models.TextChoices):
    CREATED = "CREATED"
    LOCKED = "LOCKED"  # inventory 등 모든 상태변경을 여기서 변경하도록 수정 (현재 sealed에서 변경됨)
    SEALED = "SEALED"
    SHIPPED = "SHIPPED"


class ShippingNotice(models.Model):
    code = models.CharField(
        max_length=13,
        unique=True,
        db_index=True,
        null=False,
    )
    status = models.CharField(
        max_length=20,
        choices=ShippingNoticeStatus.choices,
        default=ShippingNoticeStatus.CREATED,
    )
    template_url = models.URLField(null=True, blank=True)

    # dates
    locked_at = models.DateTimeField(null=True, blank=True)
    sealed_at = models.DateTimeField(null=True, blank=True)
    shipped_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"""Shipping Notice: {self.code}"""

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        if self.code is None or self.code == "":
            self.code = ShippingNotice.generate_usable_code()

        if self.status == ShippingNoticeStatus.LOCKED:
            self.locked_at = datetime.now()
        elif self.status == ShippingNoticeStatus.SHIPPED:
            self.shipped_at = datetime.now()
        elif self.status == ShippingNoticeStatus.SEALED:
            self.sealed_at = datetime.now()

        return super().save(force_insert, force_update, using, update_fields)

    def change_status_locked(self):
        self.status = ShippingNoticeStatus.LOCKED
        self.locked_at = datetime.now()

    def change_status_sealed(self):
        self.status = ShippingNoticeStatus.SEALED
        self.sealed_at = datetime.now()

    def change_status_shipped(self):
        self.status = ShippingNoticeStatus.SHIPPED
        self.shipped_at = datetime.now()

    @staticmethod
    def generate_usable_code():
        code = ""
        is_unique = False

        while not is_unique:
            code = ShippingNotice._make_code()
            if ShippingNotice.objects.filter(code=code).count() == 0:
                is_unique = True

        return code

    @staticmethod
    def _make_code():
        _today = date.today()
        _tomorrow = _today + timedelta(days=1)
        today = _today.isoformat()[2:].replace("-", "")

        today_notices_count = ShippingNotice.objects.filter(
            created_at__gte=_today, created_at__lt=_tomorrow
        ).count()
        sequence = f"{today_notices_count + 1}".zfill(2)
        return f"""SHP-{today}-{sequence}"""


class ShippingNoticeItem(models.Model):
    notice = models.ForeignKey(
        ShippingNotice, on_delete=models.CASCADE, related_name="shipping_notice_item"
    )
    inventory = models.OneToOneField(to=Inventory, on_delete=models.PROTECT)
class ShippingNoticeLog(Log):
    notice = models.ForeignKey(ShippingNotice, on_delete=models.DO_NOTHING)


