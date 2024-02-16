from django.contrib import admin

from core.admin import BaseAdmin
from currency.models import Currency


@admin.register(Currency)
class CurrencyAdmin(BaseAdmin):
    list_display = (
        'pk',
        'charcode',
        'rate',
        'created',
        'modified',
        'is_ictive',
    )
    search_fields = ('charcode',)
