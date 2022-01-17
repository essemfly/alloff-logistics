from datetime import date, datetime, timedelta
from django.db import models, transaction

from order.models import Order


from .common import Log
from .inventory import Inventory, InventoryStatus
from .package import Package, PackageStatus


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
        return self.code

    def change_status(self, request, status):
        # if status == self.status:  # same status
        #     return
        _old_status = self.status

        if status == ShippingNoticeStatus.LOCKED:
            self.change_status_locked(request=request)
        elif status == ShippingNoticeStatus.SHIPPED:
            self.change_status_shipped(request=request)
        elif status == ShippingNoticeStatus.SEALED:
            self.change_status_sealed(request=request)

        try:
            with transaction.atomic():
                ShippingNoticeLog.objects.create(
                    notice=self,
                    description=f"change status {self.status} >> {status}",
                    created_by=request.user,
                    field_name="status",
                    before=self.status,
                    after=status,
                )
                self.status = status
                self.save()
        except:
            # rollback (if any)
            self.status = _old_status
            pass

    def save(self, *args, **kwargs):
        if self.code is None or self.code == "":
            self.code = self._generate_usable_code()

        return super().save(*args, **kwargs)

    def change_status_locked(self, request):
        self.status = ShippingNoticeStatus.LOCKED
        self.locked_at = datetime.now()
        for item in self.items:
            item.inventory.change_status(
                request=request,
                status=InventoryStatus.SHIPPING_PENDING,
            )

    def change_status_sealed(self, request):
        self.status = ShippingNoticeStatus.SEALED
        self.sealed_at = datetime.now()

        # create package
        self._create_packages()

    def change_status_shipped(self, request):
        self.status = ShippingNoticeStatus.SHIPPED
        self.shipped_at = datetime.now()

    def _generate_usable_code(self):
        code = ""
        is_unique = False

        while not is_unique:
            code = _make_code()
            if ShippingNotice.objects.filter(code=code).count() == 0:
                is_unique = True
        return code

    def _create_packages(self):
        packages = {}
        for item in self.items:
            inventory = item.inventory
            order_id = inventory.order_id
            if order_id not in packages:
                order = Order.objects.get(id=order_id)
                packages[order_id] = Package.objects.create(
                    status=PackageStatus.DELIVERY_PREPARING,
                    related_order_item_ids=[item.order_item_id],
                    customer_name=order.customer_name,
                    customer_contact=order.customer_contact,
                    base_address=order.base_address,
                    detail_address=order.detail_address,
                    postal_code=order.postal_code,
                    delivery_note=order.delivery_note,
                )
            else:
                packages[order_id].related_order_item_ids.append(item.order_item_id)

            inventory.package = packages[order_id]
            inventory.save()

    @property
    def items(self):
        return ShippingNoticeItem.objects.filter(notice=self)


class ShippingNoticeItem(models.Model):
    notice = models.ForeignKey(
        ShippingNotice, on_delete=models.CASCADE, related_name="shipping_notice_item"
    )
    order_item_id = models.CharField(
        max_length=50,
    )
    inventory = models.OneToOneField(Inventory, on_delete=models.PROTECT)

    def __str__(self):
        return f"""[{self.notice.code}] {self.inventory.product_name} ({self.inventory.product_option})"""


class ShippingNoticeLog(Log):
    notice = models.ForeignKey(ShippingNotice, on_delete=models.DO_NOTHING)


def _make_code():
    _today = date.today()
    _tomorrow = _today + timedelta(days=1)
    today = _today.isoformat()[2:].replace("-", "")

    today_notices_count = ShippingNotice.objects.filter(
        created_at__gte=_today, created_at__lt=_tomorrow
    ).count()
    sequence = f"{today_notices_count + 1}".zfill(2)
    return f"""SHP-{today}-{sequence}"""
