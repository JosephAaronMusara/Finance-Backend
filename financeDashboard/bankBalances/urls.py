from django.urls import path
from . import views

urlpatterns = [
    path('currency/', views.CurrencyLC.as_view(), name='currency-lc'),
    path('currency/<int:pk>/', views.CurrencyRUD.as_view(), name='currency-rud'),
    path('currentasserts/', views.CurrentAssetsLC.as_view(), name='currentasserts-lc'),
    path('currentasserts/<int:pk>/', views.CurrentAssetsRUD.as_view(), name='currentasserts-rud'),
    path('overdraft/', views.NetCurrentAssetsLC.as_view(), name='od-lc'),
    path('overdraft/<int:pk>/', views.NetCurrentAssetsRUD.as_view(), name='od-rud'),
    path('grants/', views.UnutilizedGrantLC.as_view(), name='ug-lc'),
    path('grants/<int:pk>/', views.UnutilizedGrantRUD.as_view(), name='ug-rud'),
]
