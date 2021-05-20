from django.urls import path
from .views import api_list, api_retrieve, auth_api_list, auth_api_detail, redirect_to_api


urlpatterns = [
    path('', redirect_to_api),
    path('api/', api_list, name='api'),                # api/ and api/<int:pk>/ is open for use by all users
    path('api/<int:pk>/', api_retrieve, name='api_retrieve'),
    path('auth/', auth_api_list, name='auth'),         # auth/ and auth/<int:pk>/ is limited only for authorised users
    path(r'auth/<int:pk>/', auth_api_detail, name='auth_detail'),
]
