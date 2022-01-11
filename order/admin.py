from django.contrib import admin

from order.models import LogisticsOrder, Brand, Product


admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(LogisticsOrder)
