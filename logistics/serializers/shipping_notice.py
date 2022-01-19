from django_grpc_framework import proto_serializers
from logistics.models import ShippingNotice
from logistics.protos.shipping_notice_proto import shipping_notice_pb2


class ShippingNoticeProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = ShippingNotice
        proto_class = shipping_notice_pb2.ShippingNotice
        fields = "__all__"
