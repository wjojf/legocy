from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
import api.views as views 


urlpatterns = [ 
    path('', views.APIHomeView.as_view(), name='api-home'),
    path('get-token/', obtain_auth_token, name='api-obtain-token'),
    
    path('series/', views.LegoSeriesApiView.as_view(), name='api-series'),
    path('series/create/', views.AddLegoSeriesView.as_view(), name='api-add-series'),
    
    path('sets/', views.LegoSetsApiView.as_view(), name='api-sets'),
    path('sets/<int:pk>', views.LegoSetDetailApiView.as_view(), name='api-set'),
    path('sets/create/', views.AddLegoSetApiView.as_view(), name='api-create-set'),
    path('sets/update/<int:pk>', views.UpdateLegoSetApiView.as_view(), name='api-update-set'),

    path('images/', views.LegoSetsImagesApiView.as_view(), name='api-images'),
    
    path('marketitems/', views.MarketItemApiView.as_view(), name='api-marketitems'),
    path('marketitems/create/', views.AddMarketItemApiView.as_view(), name='api-create-marketitem'),
    
]