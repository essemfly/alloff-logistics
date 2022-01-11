from django.contrib import admin

from logistics.models import Package

# import only. register each files and
from .inventory import InventoryAdmin
from .received_item import ReceivedItemAdmin
from .shipping_notice import ShippingNoticeAdmin


admin.site.register(Package)
