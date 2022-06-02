from django.contrib import admin
from provider.models import Provider

class ProviderAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','phone','language','currency')

admin.site.register(Provider, ProviderAdmin)
