from django.contrib import admin
from .models import *

# Did this for testing purposes, but mainly no need since I just want to focus on API
admin.site.register(Currency)
admin.site.register(NetCurrentAsset)
admin.site.register(Total)
admin.site.register(CurrentAsset)
admin.site.register(UnutilizedGrant)