from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
import api.views as api_views 
import core.views as core_views 
import marketplace.views as marketplace_views 


urlpatterns = [ 
    path('', api_views.APIHomeView.as_view(), name='api-home'),
    path('get-token/', obtain_auth_token, name='api-obtain-token'),
    
    path('series/', core_views.LegoSeriesApiView.as_view(), name='api-series'),
    path('series/create/', core_views.AddLegoSeriesView.as_view(), name='api-add-series'),
    
    path('sets/', core_views.LegoSetsApiView.as_view(), name='api-sets'),
    path('sets/<int:pk>', core_views.LegoSetDetailApiView.as_view(), name='api-set'),
    path('sets/create/', core_views.AddLegoSetApiView.as_view(), name='api-create-set'),
    path('sets/update/<int:pk>', core_views.UpdateLegoSetApiView.as_view(), name='api-update-set'),

    path('images/', core_views.LegoSetsImagesApiView.as_view(), name='api-images'),
    
    path('marketitems/', marketplace_views.MarketItemApiView.as_view(), name='api-marketitems'),
    path('marketitems/create/', marketplace_views.AddMarketItemApiView.as_view(), name='api-create-marketitem'),
    path('marketitems/update/<int:pk>', marketplace_views.UpdateMarketItemApiView.as_view(), name='update-market-item'),

]