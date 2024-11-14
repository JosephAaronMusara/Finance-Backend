from django.contrib import admin
from django.urls import path, include
from bankBalances import urls as app_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(app_urls)),
]
