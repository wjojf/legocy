from rest_framework import serializers
from core.serializers import LegoSetSerializer, UserSerializer

from core.models import LegoSet
from .models import MarketItem, MarketItemImage
from django.contrib.auth import get_user_model
User = get_user_model()


class MarketItemSerializer(serializers.ModelSerializer):
    lego_set = LegoSetSerializer()
    seller = UserSerializer()


    class Meta:
        model = MarketItem
        fields = '__all__'


class MarketItemBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketItem
        fields = '__all__'