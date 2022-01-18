from django_grpc_framework import generics

from logistics.models import ShippingNotice
from logistics.serializers.shipping_notice import ShippingNoticeProtoSerializer


class ShippingNoticeService(generics.ModelService):
    queryset = ShippingNotice.objects.all()
    serializer_class = ShippingNoticeProtoSerializer
