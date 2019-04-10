from django.contrib import admin
from .models import Transaction


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('description', 'category',
                    'amount', 'is_activated', 'user')
    list_editable = ('is_activated',)
    search_fields = ('description', 'category')


admin.site.register(Transaction, TransactionAdmin)
