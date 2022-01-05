from django.contrib import admin, messages
from django.utils.translation import ngettext
from logistics.models.common import Log


from logistics.models.received_item import ReceivedItem, ReceivedItemStatus


from .helpers import create_copy_button, create_filter_button, format_date

received_item_status = {
    "SOURCING_REQUIRED": "발주 필요",
    "ON_RECEIVING": "입고 중",
    "RECEIVED": "입고 완료",
    "OUT_OF_STOCK": "취소됨 (재고부족)",
    "CANCELED": "취소됨 (고객 취소)",
}


@admin.register(ReceivedItem)
class ReceivedItemAdmin(admin.ModelAdmin):

    list_display = ('__str__', 'id', 'product_name',
                    'filterable_brand', 'status', 'copyable_code', 'created',)
    list_filter = ('status', 'created_at', )
    search_fields = ('product_name', 'product_brand', 'code')

    readonly_fields = ['log', ]

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
        'make_on_receiving',
        'make_received',
        'make_out_of_stock',
        'make_canceled',
    ]

    @admin.action(description='Mark status as SOURCING_REQUIRED',)
    def make_sourcing_required(self, request, queryset):
        queryset.update(status=ReceivedItemStatus.SOURCING_REQUIRED)

    @admin.action(description='Mark status as ON_RECEIVING',)
    def make_on_receiving(self, request, queryset):
        queryset.update(status=ReceivedItemStatus.ON_RECEIVING)

    @admin.action(description='Mark status as RECEIVED',)
    def make_received(self, request, queryset):
        queryset.update(status=ReceivedItemStatus.RECEIVED)

    @admin.action(description='Mark status as OUT_OF_STOCK',)
    def make_out_of_stock(self, request, queryset):
        queryset.update(status=ReceivedItemStatus.OUT_OF_STOCK)

    @admin.action(description='Mark status as CANCELED',)
    def make_canceled(self, request, queryset):
        queryset.update(status=ReceivedItemStatus.CANCELED)

    def save_model(self, request, obj, form, change):
        # todo: logging detail changes
        # request_body = request.POST.dict()
        # intance = obj.to_dict()
        if change:
            new_log = Log.objects.create(
                description="change status", created_by=request.user)
            obj.log.add(new_log)
        return super().save_model(request, obj, form, change)


def get_change_status_message(field_name, status, number):
    return ngettext(
        f'%d {field_name} was successfully marked status as {status}.',
        f'%d {field_name}s were successfully marked status as {status}.',
        number,
    ) % number
