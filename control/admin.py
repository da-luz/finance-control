from django.contrib import admin

from control.models import Category, Transaction


admin.site.register(Category, admin.ModelAdmin)
admin.site.register(Transaction, admin.ModelAdmin)
