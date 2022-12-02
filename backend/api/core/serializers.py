from rest_framework import serializers
from core.models import LegoSeries, LegoSet, LegoSetImage
from django.contrib.auth import get_user_model
User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        exclude = ('password', 'first_name', 'last_name')


class LegoSeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = LegoSeries
        fields = '__all__'


class LegoSetSerializer(serializers.ModelSerializer):
    series = LegoSeriesSerializer(read_only=True)
    
    class Meta:
        model = LegoSet
        fields = '__all__'


class LegoSetBasicSerializer(serializers.ModelSerializer):
    '''
        Same as LegoSetSerializer except series representation 
        Will be used in CreateAPIView with passing 'series' as id (not as an object)
    '''
    
    class Meta:
        model = LegoSet
        fields = '__all__'


class LegoSetImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = LegoSetImage
        fields = '__all__'