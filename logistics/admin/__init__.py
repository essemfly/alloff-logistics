from django.contrib import admin

from logistics.models import Inventory, Package, ShippingNotice

# import only. register each files and
from .received_item import ReceivedItemAdmin
from .shipping_notice import ShippingNoticeAdmin


admin.site.register(Inventory)
admin.site.register(Package)
# admin.site.register(ShippingNotice)
