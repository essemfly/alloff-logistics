from django.contrib import admin

from order.models import Order, Brand, Product


admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(Order)
