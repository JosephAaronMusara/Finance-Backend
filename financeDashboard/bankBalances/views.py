from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from django.http import JsonResponse
import requests

# # USD is the base currency
# url = 'https://v6.exchangerate-api.com/v6/6459d7c694287d1105f6044c/latest/USD'

# response = requests.get(url)
# data = response.json()
# print(data)
		

# crncies

class CurrencyLC(generics.ListCreateAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    filterset_fields = ['currency_code']
    search_fields = ['currency_code']
    ordering_fields = ['currency_code']
    
class CurrencyRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    
#CA
class CurrentAssetsLC(generics.ListCreateAPIView):
    queryset = CurrentAsset.objects.all()
    serializer_class = CurrentAssetSerializer
    filterset_fields = ['currency']
    search_fields = ['currency']
    ordering_fields = ['currency','amount']

class CurrentAssetsRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = CurrentAsset.objects.all()
    serializer_class = CurrentAssetSerializer
    
#OD
class NetCurrentAssetsLC(generics.ListCreateAPIView):
    queryset = NetCurrentAsset.objects.all()
    serializer_class = NetCurrentAssetsSerializer
    ordering_fields = ['amount']
    
class NetCurrentAssetsRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = NetCurrentAsset.objects.all()
    serializer_class = NetCurrentAssetsSerializer
    
#Unutilised Grants
class UnutilizedGrantLC(generics.ListCreateAPIView):
    queryset = UnutilizedGrant.objects.all()
    serializer_class = UnutilizedGrantSerializer
    filterset_fields = ['currency', 'donor']
    search_fields = ['currency','donor']
    ordering_fields = ['amount']
    
class UnutilizedGrantRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = UnutilizedGrant.objects.all()
    serializer_class = UnutilizedGrantSerializer