from django_grpc_framework import generics

from logistics.models import ReceivedItem
from logistics.serializers.received_item import ReceivedItemProtoSerializer


class ReceivedItemService(generics.ModelService):
    queryset = ReceivedItem.objects.all()
    serializer_class = ReceivedItemProtoSerializer
