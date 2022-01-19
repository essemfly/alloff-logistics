from django_grpc_framework import generics

from logistics.models import Package
from logistics.serializers.package import PackageProtoSerializer


class PackageService(generics.ModelService):
    queryset = Package.objects.all()
    serializer_class = PackageProtoSerializer
