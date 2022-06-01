from rest_framework import serializers
from area.models import Area

class AreaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Area
        fields = ('id', 'name', 'price', 'geojson')