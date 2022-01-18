from logistics.protos.inventory_proto import inventory_pb2_grpc

from .services.inventory import InventoryService


def grpc_handlers(server):
    inventory_pb2_grpc.add_InventoryControllerServicer_to_server(
        InventoryService.as_servicer(), server
    )

    pass
