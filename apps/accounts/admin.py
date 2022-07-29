from django.contrib import admin
from .models import Account


class AccountAmin(admin.ModelAdmin):
    list_display = ('email', 'id', 'full_name')


admin.site.register(Account, AccountAmin)
