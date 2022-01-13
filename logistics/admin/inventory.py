from django.contrib import admin
from logistics.models.inventory import Inventory, InventoryStatus, InventoryLog

from lib.helpers import create_copy_button, create_filter_button, format_date
from lib.admin import LogTabularInline


inventory_status = {
    "CREATED": "생성됨",
    "PROCESSING_NEEDED": "프로세싱 필요함",
    "IN_STOCK": "재고 있음",
    "SHIPPING_PENDING": "발송 준비중",
    "SHIPPED": "발송됨",
}


class InventoryLogInline(LogTabularInline):
    model = InventoryLog


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):

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
    inlines = [
        InventoryLogInline,
    ]

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
        "make_created",
        "make_in_stock",
        "make_processing_needed",
        "make_shipped",
        "make_shipping_pending",
    ]

    @admin.action(
        description="Mark status as CREATED",
    )
    def make_created(self, *args, **kwargs):
        self._change_status(status=InventoryStatus.CREATED, *args, **kwargs)

    @admin.action(
        description="Mark status as IN_STOCK",
    )
    def make_in_stock(self, *args, **kwargs):
        self._change_status(status=InventoryStatus.IN_STOCK, *args, **kwargs)

    @admin.action(
        description="Mark status as PROCESSING_NEEDED",
    )
    def make_processing_needed(self, *args, **kwargs):
        self._change_status(status=InventoryStatus.PROCESSING_NEEDED, *args, **kwargs)

    @admin.action(
        description="Mark status as SHIPPED",
    )
    def make_shipped(self, *args, **kwargs):
        self._change_status(status=InventoryStatus.SHIPPED, *args, **kwargs)

    @admin.action(
        description="Mark status as SHIPPING_PENDING",
    )
    def make_shipping_pending(self, *args, **kwargs):
        self._change_status(status=InventoryStatus.SHIPPING_PENDING, *args, **kwargs)

    def _change_status(self, request, queryset, status):
        [
            instance.change_status(
                request=request,
                status=status,
            )
            for instance in queryset.all()
        ]
