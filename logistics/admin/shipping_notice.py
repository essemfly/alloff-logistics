from django.contrib import admin
from lib.helpers import format_date


from logistics.models.shipping_notice import (
    ShippingNotice,
    ShippingNoticeItem,
    ShippingNoticeStatus,
    ShippingNoticeLog,
)
from lib.admin import LogTabularInline


class ShippingNoticeLogInline(LogTabularInline):
    model = ShippingNoticeLog


class ShippingNoticeItemInline(admin.StackedInline):
    model = ShippingNoticeItem
    extra = 3


@admin.register(ShippingNotice)
class ShippingNoticeAdmin(admin.ModelAdmin):

    list_display = (
        "__str__",
        "id",
        "status",
        "created",
        "locked",
        "sealed",
        "shipped",
    )
    list_filter = ("status",)
    search_fields = ("code",)

    readonly_fields = (
        "created_at",
        "locked_at",
        "sealed_at",
        "shipped_at",
    )

    inlines = [
        ShippingNoticeItemInline,
        ShippingNoticeLogInline,
    ]

    @admin.display(description="created")
    def created(self, obj):
        return format_date(obj.created_at)

    @admin.display(description="locked")
    def locked(self, obj):
        return format_date(obj.locked_at)

    @admin.display(description="sealed")
    def sealed(self, obj):
        return format_date(obj.sealed_at)

    @admin.display(description="shipped")
    def shipped(self, obj):
        return format_date(obj.shipped_at)

    # actions
    actions = ["make_created", "make_locked", "make_sealed", "make_shipped"]

    @admin.action(
        description="Mark status as CREATED",
    )
    def make_created(self, *args, **kwargs):
        self._change_status(status=ShippingNoticeStatus.CREATED, *args, **kwargs)

    @admin.action(
        description="Mark status as LOCKED",
    )
    def make_locked(self, *args, **kwargs):
        self._change_status(status=ShippingNoticeStatus.LOCKED, *args, **kwargs)

    @admin.action(
        description="Mark status as SEALED",
    )
    def make_sealed(self, *args, **kwargs):
        self._change_status(status=ShippingNoticeStatus.SEALED, *args, **kwargs)

    @admin.action(
        description="Mark status as SHIPPED",
    )
    def make_shipped(self, *args, **kwargs):
        self._change_status(status=ShippingNoticeStatus.SHIPPED, *args, **kwargs)

    def _change_status(self, request, queryset, status):
        [
            instance.change_status(
                request=request,
                status=status,
            )
            for instance in queryset.all()
        ]
