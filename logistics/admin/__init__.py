from django.contrib import admin


# import only. register each files and
from .inventory import InventoryAdmin
from .received_item import ReceivedItemAdmin
from .shipping_notice import ShippingNoticeAdmin
from .package import PackageAdmin
