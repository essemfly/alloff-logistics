from django_grpc_framework import proto_serializers
from logistics.models import Inventory
from logistics.protos.inventory_proto import inventory_pb2


class InventoryProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = Inventory
        proto_class = inventory_pb2.Inventory
        fields = "__all__"
