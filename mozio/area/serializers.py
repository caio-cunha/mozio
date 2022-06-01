from rest_framework import serializers
from area.models import Area
from provider.models import Provider

class AreaSerializer(serializers.ModelSerializer):

    provider = serializers.PrimaryKeyRelatedField(queryset=Provider.objects.all(), write_only=True, required=True)

    class Meta:
        model = Area
        fields = ('id', 'name', 'price', 'provider', 'geojson')