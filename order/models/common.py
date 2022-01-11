import uuid
from django.db import models


class Brand(models.Model):
    key = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50,)

    def __str__(self):
        return f"#{self.id} {self.name} ({self.key})"


class Product(models.Model):
    key = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    brand = models.ForeignKey(Brand, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=50,)
    size = models.CharField(max_length=50,)
    color = models.CharField(max_length=50,)

    @property
    def brand_id(self):
        return self.brand.id

    @property
    def brand_name(self):
        return self.brand.name

    def __str__(self):
        return f"#{self.id} {self.name} ({self.key})"
