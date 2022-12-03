from django.urls import path

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView
)
from api.views import MyTokenObtainPairView
import api.views as api_views 
import api.core.views as core_views 


router = DefaultRouter()
router.register(r'series', core_views.LegoSeriesViewSet)
router.register(r'sets', core_views.LegoSetViewSet)

urlpatterns = [ 
    path('', api_views.APIHomeView.as_view(), name='api-home'),
    
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify', TokenVerifyView.as_view(), name='token_verify'),

] + router.urls
