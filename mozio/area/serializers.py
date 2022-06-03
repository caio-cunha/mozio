from rest_framework import serializers
from area.models import Area
from provider.models import Provider
from provider.serializers import ProviderSerializer

class AreaSerializer(serializers.ModelSerializer):

    provider = serializers.PrimaryKeyRelatedField(queryset=Provider.objects.all(), write_only=False, required=False)

    class Meta:
        model = Area
        fields = ('id', 'name', 'price', 'provider', 'geojson')


class AreaPatchSerializer(serializers.ModelSerializer):

    provider = serializers.PrimaryKeyRelatedField(queryset=Provider.objects.all(), write_only=False, required=False)

    class Meta:
        model = Area
        fields = ('id', 'name', 'price', 'provider', 'geojson')
