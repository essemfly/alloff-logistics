from logistics.protos.inventory_proto import inventory_pb2_grpc
from logistics.protos.package_proto import package_pb2_grpc
from logistics.protos.received_item_proto import received_item_pb2_grpc
from logistics.protos.shipping_notice_proto import shipping_notice_pb2_grpc


from .services.inventory import InventoryService
from .services.package import PackageService
from .services.received_item import ReceivedItemService
from .services.shipping_notice import ShippingNoticeService


def grpc_handlers(server):
    inventory_pb2_grpc.add_InventoryControllerServicer_to_server(
        InventoryService.as_servicer(), server
    )
    package_pb2_grpc.add_PackageControllerServicer_to_server(
        PackageService.as_servicer(), server
    )
    received_item_pb2_grpc.add_ReceivedItemControllerServicer_to_server(
        ReceivedItemService.as_servicer(), server
    )
    shipping_notice_pb2_grpc.add_ShippingNoticeControllerServicer_to_server(
        ShippingNoticeService.as_servicer(), server
    )
