from django.contrib import admin

from order.models import Payment

# import only. register each files and
from .order import OrderAdmin

admin.site.register(Payment)
