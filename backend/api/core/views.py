from api.core.serializers import (LegoSeriesSerializer, LegoSetBasicSerializer,
                                  LegoSetImageSerializer, LegoSetSerializer)
from core.models import LegoSeries, LegoSet, LegoSetImage
from core.utils import FilteredListMixin
from rest_framework import generics, status, viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class LegoSeriesViewSet(viewsets.ModelViewSet):
    queryset = LegoSeries.objects.all()
    serializer_class = LegoSeriesSerializer

    def get_permissions(self):

        if self.action in ("list", "retrieve"):
            permissions = (IsAuthenticated, )
        else:
            permissions = (IsAdminUser, )

        return [permission() for permission in permissions]

    def list(self, request, *args, **kwargs):
        series_qs, qs_status = FilteredListMixin.filter_qs(request, self.queryset)
        data = self.serializer_class(series_qs, many=True).data
        
        return Response({
            "data": data,
            "meta": {
                "type": "series_list",
                "OK":True if qs_status==status.HTTP_200_OK else False
            }
        }, status=qs_status)

    def retrieve(self, request, pk=None):
        try:
            obj = self.queryset.get(pk=pk)
        except Exception:
            return Response({
                "data": None,
                "meta": {
                    "error": 201,
                    "error_message": f"Could not find a LegoSet with ID {pk}",
                    "pk_received": pk
                },
            },status=status.HTTP_404_NOT_FOUND)     
        
        serializer = self.serializer_class(obj)
        return Response({
            "data": serializer.data,
            "meta": {
                "type": "series_detail",
                "OK":True,
            }
        })


class LegoSetViewSet(viewsets.ModelViewSet):
    queryset = LegoSet.objects.all()

    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return LegoSetSerializer
        return LegoSetBasicSerializer
    
    def get_permissions(self):

        if self.action in ("list", "retrieve"):
            permissions = (IsAuthenticated, )
        else:
            permissions = (IsAdminUser, )

        return [permission() for permission in permissions]

    def list(self, request, *args, **kwargs):
        sets_qs, qs_status = FilteredListMixin.filter_qs(request, self.queryset)
        data = self.get_serializer_class()(sets_qs, many=True).data

        return Response({
            "data": data,
            "meta": {
                "type": "set_list",
                "OK":True if qs_status==status.HTTP_200_OK else False
            }
        }, status=qs_status)

    def retrieve(self, request, pk=None):
        try:
            obj = self.queryset.get(pk=pk)
        except Exception:
            return Response({
                "data": None,
                "meta": {
                    "pk_received": pk,
                    "error_message": f'''
                    Could not find a LegoSet obj with ID {pk}
                    '''
                }
            }, status=status.HTTP_400_BAD_REQUEST)
        
        data = self.get_serializer_class()(obj).data
        return Response({
            "data": data,
            "meta": {
                "type": "set_detail",
                "OK":True
            }
        })
