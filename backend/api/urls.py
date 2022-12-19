import api.marketplace.views as marketplace_views
import api.core.views as core_views
import api.views as api_views
from api.views import MyTokenObtainPairView, RegisterView
from django.urls import path

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView
)
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView
)

router = DefaultRouter()
router.register(r'series', core_views.LegoSeriesViewSet)
router.register(r'sets', core_views.LegoSetViewSet)
router.register(r'marketitems', marketplace_views.MarketItemViewSet, basename='MarketItem')

urlpatterns = [
    path('', api_views.APIHomeView.as_view(), name='api-home'),
    path('register/', RegisterView.as_view(), name='register'),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify', TokenVerifyView.as_view(), name='token_verify'),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "docs/",
        SpectacularSwaggerView.as_view(
            template_name="swagger-ui.html",
            url_name="schema",
        ),
        name="swagger-ui",
    ),
] + router.urls
