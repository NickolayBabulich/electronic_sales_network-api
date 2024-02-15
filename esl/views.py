from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework import status, permissions, viewsets

from esl.serializers import SupplierSerializer, CommercialNetworkSerializer
from esl.models import Supplier, CommercialNetwork
from esl.filters import SellerFilter, NetworkFilter


class SupplierCreateAPIView(CreateAPIView):
    serializer_class = SupplierSerializer


class SupplierListAPIView(ListAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    filterset_class = SellerFilter
    filter_backends = [DjangoFilterBackend]
    permission_classes = (permissions.IsAuthenticated,)


class SupplierRetrieveAPIView(RetrieveAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = (permissions.IsAuthenticated,)


class SupplierUpdateAPIView(UpdateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

    def update(self, request, *args, **kwargs):
        if request.method != 'PATCH':
            return Response({'error': 'Метод PUT не разрешен, выберите метод PATCH'},
                            status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().update(request, *args, **kwargs)


class SupplierDestroyAPIView(DestroyAPIView):
    queryset = Supplier.objects.all()


class CommercialNetworkViewSet(viewsets.ModelViewSet):
    queryset = CommercialNetwork.objects.all()
    serializer_class = CommercialNetworkSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filterset_class = NetworkFilter
    filter_backends = [DjangoFilterBackend]

    def update(self, request, *args, **kwargs):
        object = self.get_object()

        if 'debt_to_supplier' in request.data and request.data['debt_to_supplier'] != object.debt_to_supplier:
            return Response(
                {
                    'error': 'Запрещено обновлять поле debt_to_supplier - '
                             '"задолженность перед поставщиком" через API интерфейс'},
                status=status.HTTP_400_BAD_REQUEST)

        return super().update(request, *args, **kwargs)
