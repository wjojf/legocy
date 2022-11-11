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

#TODO:
class UpdateMarketItemApiView(APIView):
    permission_classes = (IsItemOwner, )
    