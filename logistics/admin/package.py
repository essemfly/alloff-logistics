from django.contrib import admin, messages
from logistics.models.package import (
    Package,
    PackageStatus,
    PackageRemarkRecord,
    PackageLog,
)
from lib.helpers import format_date
from lib.admin import LogTabularInline

from logistics.models import Inventory


class PackageRelatedInventoryInline(admin.TabularInline):
    model = Inventory
    fields = ("__str__",)
    readonly_fields = ["__str__"]
    extra = 0


class PackageRemarkRecordInline(admin.TabularInline):
    model = PackageRemarkRecord
    fields = (
        "record_type",
        "description",
        "created_by",
    )
    readonly_fields = ["created_by"]
    extra = 1


class PackageLogInline(LogTabularInline):
    model = PackageLog


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):

    list_display = (
        "__str__",
        "status",
        "customer_name",
        "customer_contact",
        "full_address",
        "tracking_number",
        "created",
    )
    list_filter = (
        "status",
        "created_at",
    )
    search_fields = (
        "customer_name",
        "customer_contact",
        "base_address",
        "tracking_number",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
        "deleted_at",
    )

    inlines = (
        PackageRelatedInventoryInline,
        PackageRemarkRecordInline,
        PackageLogInline,
    )

    @admin.display(description="full address")
    def full_address(self, obj):
        return f"{obj.base_address} {obj.detail_address} ({obj.postal_code})"

    @admin.display(description="created")
    def created(self, obj):
        return format_date(obj.created_at)

    # actions
    actions = [
        "make_cancel_requested",
    ]

    @admin.action(
        description="Mark status as CANCEL_REQUESTED",
    )
    def make_cancel_requested(self, *args, **kwargs):
        self._change_status(status=PackageStatus.CANCEL_REQUESTED, *args, **kwargs)

    def _change_status(self, request, queryset, status):
        for instance in queryset:
            instance.change_status(
                request=request,
                status=status,
            )
