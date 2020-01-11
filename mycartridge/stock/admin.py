from django.contrib import admin
from .models import Data


class StockAdmin(admin.ModelAdmin):
    list_filter = ['area', 'industry']
    search_fields = ['name', 'code']


admin.site.register(Data, StockAdmin)
