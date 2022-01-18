from django_grpc_framework import proto_serializers
from logistics.models import Package
from logistics.protos.package_proto import package_pb2


class PackageProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = Package
        proto_class = package_pb2.Package
        fields = "__all__"
