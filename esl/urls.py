from django.urls import path
from rest_framework import routers
from esl.views import (SupplierCreateAPIView,
                       SupplierListAPIView,
                       SupplierRetrieveAPIView,
                       SupplierUpdateAPIView,
                       SupplierDestroyAPIView,
                       CommercialNetworkViewSet)

router = routers.DefaultRouter()
router.register(r'network', CommercialNetworkViewSet)

urlpatterns = [
    path('supplier/create/', SupplierCreateAPIView.as_view(), name='supplier-create'),
    path('supplier/', SupplierListAPIView.as_view(), name='supplier-list'),
    path('supplier/view/<int:pk>/', SupplierRetrieveAPIView.as_view(), name='supplier-view'),
    path('supplier/edit/<int:pk>/', SupplierUpdateAPIView.as_view(), name='supplier-edit'),
    path('supplier/delete/<int:pk>/', SupplierDestroyAPIView.as_view(), name='supplier-delete')
]
urlpatterns += router.urls
