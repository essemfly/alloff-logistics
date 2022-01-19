from django_grpc_framework import generics

from logistics.models import Inventory
from logistics.serializers.inventory import InventoryProtoSerializer


class InventoryService(generics.ModelService):
    queryset = Inventory.objects.all()
    serializer_class = InventoryProtoSerializer
