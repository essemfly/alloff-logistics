from django.contrib import admin, messages
from logistics.models.received_item import (
    ReceivedItem,
    ReceivedItemStatus,
    ReceivedItemLog,
)
from lib.helpers import create_copy_button, create_filter_button, format_date
from lib.admin import LogTabularInline
from logistics.models.shipping_notice import ShippingNotice, ShippingNoticeItem


received_item_status = {
    "SOURCING_REQUIRED": "발주 필요",
    "ON_RECEIVING": "입고 중",
    "RECEIVED": "입고 완료",
    "OUT_OF_STOCK": "취소됨 (재고부족)",
    "CANCELED": "취소됨 (고객 취소)",
}


class ReceivedItemLogInline(LogTabularInline):
    model = ReceivedItemLog


@admin.register(ReceivedItem)
class ReceivedItemAdmin(admin.ModelAdmin):

    list_display = (
        "__str__",
        "id",
        "product_name",
        "filterable_brand",
        "status",
        "copyable_code",
        "created",
    )
    list_filter = (
        "status",
        "created_at",
    )
    search_fields = ("product_name", "product_brand", "code")

    readonly_fields = (
        "created_at",
        "updated_at",
        "deleted_at",
    )

    inlines = (ReceivedItemLogInline,)

    @admin.display(description="code")
    def copyable_code(self, obj):
        return create_copy_button(obj.code)

    @admin.display(description="brand")
    def filterable_brand(self, obj):
        return create_filter_button(
            "product_brand_id", obj.product_brand_id, obj.product_brand_name
        )

    @admin.display(description="created")
    def created(self, obj):
        return format_date(obj.created_at)

    # actions
    actions = [
        "make_sourcing_required",
        "make_on_receiving",
        "make_received",
        "make_out_of_stock",
        "make_canceled",
        "generate_shipping_notice",
    ]

    @admin.action(
        description="Mark status as SOURCING_REQUIRED",
    )
    def make_sourcing_required(self, *args, **kwargs):
        self._change_status(
            status=ReceivedItemStatus.SOURCING_REQUIRED, *args, **kwargs
        )

    @admin.action(
        description="Mark status as ON_RECEIVING",
    )
    def make_on_receiving(self, *args, **kwargs):
        self._change_status(status=ReceivedItemStatus.ON_RECEIVING, *args, **kwargs)

    @admin.action(
        description="Mark status as RECEIVED",
    )
    def make_received(self, *args, **kwargs):
        self._change_status(status=ReceivedItemStatus.RECEIVED, *args, **kwargs)

    @admin.action(
        description="Mark status as OUT_OF_STOCK",
    )
    def make_out_of_stock(self, *args, **kwargs):
        self._change_status(status=ReceivedItemStatus.OUT_OF_STOCK, *args, **kwargs)

    @admin.action(
        description="Mark status as CANCELED",
    )
    def make_canceled(self, *args, **kwargs):
        self._change_status(status=ReceivedItemStatus.CANCELED, *args, **kwargs)

    def _change_status(self, request, queryset, status):
        for instance in queryset:
            instance.change_status(
                request=request,
                status=status,
            )

    @admin.action(
        description="Generate shipping notice include selected items",
    )
    def generate_shipping_notice(self, request, queryset):
        if any(
            instance.status == ReceivedItemStatus.RECEIVED
            for instance in queryset.all()
        ):
            shipping_notice = ShippingNotice.objects.create()
            for instance in queryset:
                ShippingNoticeItem.objects.create(
                    order_item_id=instance.order_item_id,
                    notice=shipping_notice,
                    inventory=instance.inventory,
                )
        else:
            # error message
            messages.error(request, "ONLY Received could be collected")
