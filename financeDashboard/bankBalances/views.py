from rest_framework import generics
from .serializers import *
from django.http import JsonResponse
import requests

# # USD is the base currency
# url = 'https://v6.exchangerate-api.com/v6/6459d7c694287d1105f6044c/latest/USD'

# response = requests.get(url)
# data = response.json()
# print(data)
		
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
class BankBalanceListCreate(generics.ListCreateAPIView):
    queryset = BankBalance.objects.all()
    serializer_class = BankBalanceSerializer
    filterset_fields = ['currency','type']
    search_fields = ['currency','type','name']
    ordering_fields = ['currency','amount','type']

class BankBalanceRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BankBalance.objects.all()
    serializer_class = BankBalanceSerializer
    
class AccountReceivableListCreate(generics.ListCreateAPIView):
    queryset = AccountReceivable.objects.all()
    serializer_class = AccountReceivableSerializer

class AccountReceivableRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = AccountReceivable.objects.all()
    serializer_class = AccountReceivableSerializer