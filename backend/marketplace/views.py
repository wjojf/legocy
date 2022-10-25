from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated

from marketplace.permissions import IsItemOwner
from marketplace.models import MarketItem
from marketplace.serializers import MarketItemBasicSerializer, MarketItemSerializer

from core.views import FilteredListMixin


class MarketItemApiView(FilteredListMixin, generics.ListAPIView):
    '''GET router for all Market Items'''
    queryset = MarketItem.objects.select_related('lego_set', 'seller').all()
    serializer_class = MarketItemSerializer

    
class AddMarketItemApiView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = MarketItem.objects.all()
    serializer_class = MarketItemBasicSerializer


class UpdateMarketItemApiView(APIView):
    permission_classes = (IsAuthenticated, IsItemOwner)

    def __init__(self, **kwargs):
        self.market_item = None
        super().__init__(**kwargs)

    def post(self, request):
        self.market_item = get_object_or_404(MarketItem,
                                             id=request.data.get('id'))
        active_status = request.data.get('active')
        price = request.data.get('price')
        currency = request.data.get('currency')
        if currency is None and price is None and currency is None:
            return Response('Empty fields are passed',
                            status=status.HTTP_400_BAD_REQUEST)
        if active_status is not None:
            self.market_item.active = active_status
        if price is not None:
            self.market_item.price = price
        if currency is not None:
            self.market_item.currency = currency
        self.market_item.save()
        return Response('Success', status=status.HTTP_200_OK)
