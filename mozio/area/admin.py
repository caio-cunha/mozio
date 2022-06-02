from django.contrib import admin
from area.models import Area

class AreaAdmin(admin.ModelAdmin):
    list_display = ('id','name','price','provider_id','geojson')

admin.site.register(Area, AreaAdmin)

