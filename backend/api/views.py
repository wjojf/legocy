from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from api.jwt_serializers import MyTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

ROUTES = {
    'TODO': True
}


# Create your views here.
class APIHomeView(APIView):
    permission_classes = (AllowAny, )

    def get(self, request, *args, **kwargs):
        return Response({'message': f'Welcome to legocy API! This is home page, but you can read more at www.legocy.com/documenation/api'})


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


