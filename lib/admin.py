from django.contrib import admin


class LogTabularInline(admin.TabularInline):
    fields = (
        "description",
        "created_by",
    )
    readonly_fields = ("__str__",)
    extra = 0

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
