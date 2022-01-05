from django.contrib import admin


from logistics.models.shipping_notice import ShippingNotice, ShippingNoticeItem


class ShippingNoticeItemInline(admin.StackedInline):
    model = ShippingNoticeItem
    extra = 3


@admin.register(ShippingNotice)
class ShippingNoticeAdmin(admin.ModelAdmin):

    list_display = ('__str__', 'id', 'status',
                    'created_at', 'locked_at', 'sealed_at', 'shipped_at')
    list_filter = ('status', )
    search_fields = ('code', )

    readonly_fields = ('created_at', 'locked_at', 'sealed_at', 'shipped_at', )

    inlines = [ShippingNoticeItemInline, ]
