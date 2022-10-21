from rest_framework.views import APIView
from rest_framework import generics

from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from core.permissions import IsItemOwner

from marketplace.models import MarketItem
from marketplace.serializers import MarketItemBasicSerializer, MarketItemSerializer

from core.views import FilteredListMixin


class MarketItemApiView(FilteredListMixin, generics.ListAPIView):
    queryset = MarketItem.objects.select_related('lego_set', 'seller').all()
    serializer_class = MarketItemSerializer


class AddMarketItemApiView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = MarketItem.objects.all()
    serializer_class = MarketItemBasicSerializer
