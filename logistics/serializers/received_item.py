from django_grpc_framework import proto_serializers
from logistics.models import ReceivedItem
from logistics.protos.received_item_proto import received_item_pb2


class ReceivedItemProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = ReceivedItem
        proto_class = received_item_pb2.ReceivedItem
        fields = "__all__"
