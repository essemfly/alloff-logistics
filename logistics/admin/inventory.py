from django.contrib import admin
from logistics.models.inventory import Inventory, InventoryStatus, InventoryLog
from .helpers import create_copy_button, create_filter_button, format_date

inventory_status = {
    "PROCESSING_NEEDED": "프로세싱 필요함",
    "IN_STOCK": "재고 있음",
    "SHIPPING_PENDING": "발송 준비중",
    "SHIPPED": "발송됨",
}


class InventoryLogInline(admin.TabularInline):
    model = InventoryLog
    readonly_fields = ('__str__', )
    extra = 0

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):

    list_display = ('__str__', 'id', 'product_name',
                    'filterable_brand', 'status', 'copyable_code', 'created',)
    list_filter = ('status', 'created_at', )
    search_fields = ('product_name', 'product_brand', 'code')

    readonly_fields = ('created_at', 'updated_at', 'deleted_at', )
    inlines = [InventoryLogInline, ]

    @admin.display(description='code')
    def copyable_code(self, obj):
        return create_copy_button(obj.code)

    @admin.display(description='brand')
    def filterable_brand(self, obj):
        return create_filter_button('product_brand_id', obj.product_brand_id, obj.product_brand_name)

    @admin.display(description='created')
    def created(self, obj):
        return format_date(obj.created_at)

    # actions
    actions = [
        'make_sourcing_required',
    ]

    @admin.action(description='Mark status as SOURCING_REQUIRED',)
    def make_sourcing_required(self, request, queryset):
        instance = queryset.get()
        instance.change_status(
            request=request,
            status=InventoryStatus.SOURCING_REQUIRED,
        )
