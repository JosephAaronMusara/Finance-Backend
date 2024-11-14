from django.urls import path
from . import views

urlpatterns = [
    path('bankbalance/', views.BankBalanceListCreate.as_view(), name='bankbalance-lc'),
    path('bankbalance/<int:pk>/', views.BankBalanceRetrieveUpdateDestroy.as_view(), name='bankbalance-rud'),
    path('accountreceivable/', views.AccountReceivableListCreate.as_view(), name='accountreceivable-lc'),
    path('accountreceivable/<int:pk>/', views.AccountReceivableRetrieveUpdateDestroy.as_view(), name='accountreceivable-rud'),
]
