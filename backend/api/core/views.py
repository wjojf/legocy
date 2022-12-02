from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework import status
from django.shortcuts import get_object_or_404

from api.core.serializers import LegoSeriesSerializer, LegoSetImageSerializer, LegoSetSerializer, LegoSetBasicSerializer
from core.models import LegoSeries, LegoSet, LegoSetImage
from core.utils import FilteredListMixin

import json



# LegoSeries Views 
class LegoSeriesApiView(FilteredListMixin, generics.ListAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = LegoSeries.objects.all()
    serializer_class = LegoSeriesSerializer


class AddLegoSeriesView(generics.CreateAPIView):
    permission_classes = (IsAdminUser, )
    queryset = LegoSeries.objects.all()
    serializer_class = LegoSeriesSerializer


class LegoSetsApiView(FilteredListMixin, generics.ListAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = LegoSet.objects.select_related('series').all()
    serializer_class = LegoSetSerializer


class LegoSetDetailApiView(APIView):
    permission_classes = (IsAuthenticated, )
    
    def get(self, request, pk):
        try:
            obj = LegoSet.objects.select_related('series').get(pk=pk)
        except Exception as e:
            return Response({
                    "data": None,
                    "meta": {
                        "error": 201,
                        "error_message": "Could not find a LegoSet with ID {}".format(pk), 
                        "pk_received": pk
                    },
                },status=status.HTTP_404_NOT_FOUND)
               
    
        return Response(LegoSetSerializer(obj, many=False).data)
    

class AddLegoSetApiView(generics.CreateAPIView):
    permission_classes = (IsAdminUser, )
    queryset = LegoSet.objects.all()
    serializer_class = LegoSetBasicSerializer


#TODO: finish view
class UpdateLegoSetApiView(generics.UpdateAPIView):
    permission_classes = (IsAdminUser, )
    queryset = LegoSet.objects.all()
    serializer_class = LegoSetBasicSerializer

        
# LegoSetImage Views
class LegoSetsImagesApiView(FilteredListMixin, generics.ListAPIView):
    queryset = LegoSetImage.objects.select_related('lego_set').all()
    serializer_class = LegoSetImageSerializer