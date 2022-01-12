from django.contrib import admin
from lib.helpers import create_copy_button, format_date
from order.models import Order, OrderItem


class OrderItemInline(admin.StackedInline):
    model = OrderItem
    extra = 2
    readonly_fields = (
        "created_at",
        "updated_at",
        "ordered_at",
        "delivery_started_at",
        "delivery_finished_at",
        "cancel_requested_at",
        "cancel_finished_at",
        "confirmed_at",
    )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = ("__str__", "order_status", "copyable_code", "created")
    list_filter = (
        "order_status",
        "created_at",
    )
    search_fields = ("alloff_order_id",)

    readonly_fields = (
        "created_at",
        "updated_at",
        "ordered_at",
        "delivery_started_at",
        "delivery_finished_at",
        "cancel_requested_at",
        "cancel_finished_at",
        "confirmed_at",
    )
    inlines = [
        OrderItemInline,
    ]

    @admin.display(description="alloff order id")
    def copyable_code(self, obj):
        return create_copy_button(obj.alloff_order_id)

    @admin.display(description="created")
    def created(self, obj):
        return format_date(obj.created_at)
