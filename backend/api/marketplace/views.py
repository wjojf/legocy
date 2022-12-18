from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from api.marketplace.permissions import IsItemOwner
from marketplace.models import MarketItem
from api.marketplace.serializers import MarketItemBasicSerializer, MarketItemSerializer

from core.utils import FilteredListMixin


class MarketItemViewSet(viewsets.ModelViewSet):

    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return MarketItemSerializer
        return MarketItemBasicSerializer

    def get_permissions(self):

        if self.action in ("list", "retrieve", "create"):
            permissions = (IsAuthenticated, )
        else:
            permissions = (IsItemOwner, IsAuthenticated)

        return [permission() for permission in permissions]

    def get_queryset(self):
        queryset = MarketItem.objects.all()
        qs, qs_status = FilteredListMixin.filter_qs(self.request, queryset)
        if qs_status != status.HTTP_200_OK:
            return queryset
        return qs

    def retrieve(self, request, pk):
        try:
            obj = self.get_queryset().get(pk=pk)
        except Exception as e:
            return Response({
                "data": None,
                "meta": {
                    "pk_received": pk,
                    "error_message": f'{e}'
                }
            }, status=status.HTTP_400_BAD_REQUEST)

        data = self.get_serializer_class()(obj).data
        return Response({
            "data": data,
            "meta": {
                "type": "marketitem_detail",
                "OK": True
            }
        }, status=status.HTTP_200_OK)
