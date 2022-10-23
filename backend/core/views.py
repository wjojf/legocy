from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from .serializers import LegoSeriesSerializer, LegoSetImageSerializer, LegoSetSerializer, LegoSetBasicSerializer
from .models import LegoSeries, LegoSet, LegoSetImage
from .permissions import IsItemOwner

import json


class FilteredListMixin(object):
    def get(self, request, *args, **kwargs):
        try:
            body = json.loads(request.body)
        except Exception as e:
            print(e)
            body = {}

        if 'filter_' in body:
            for k, v in body['filter_'].items():
                filter_string = f'self.queryset.filter({k}={v})'
                print(filter_string)
                try:
                    self.queryset = eval(filter_string)
                except Exception as e:
                    continue
        
        return super().get(request, *args, **kwargs)


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
            return Response({'error': str(e)})
    
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