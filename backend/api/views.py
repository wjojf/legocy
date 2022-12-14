from api.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from api.jwt_serializers import MyTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


# Create your views here.
class APIHomeView(APIView):
    permission_classes = (AllowAny, )

    def get(self, request, *args, **kwargs):
        return Response({
            'data': '''
            Welcome to legocy API!
             This is home page, but you can read more at www.legocy.com/documenation/api''',
            'meta': {
                'home_page': True
            }})


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


# view for registering users
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
