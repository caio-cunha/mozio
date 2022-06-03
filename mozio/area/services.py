"""
Bussines Logic

Author: Caio Henrique 
Email: caiocomputacao2014@gmail.com
"""

from area.models import Area
from area.serializers import AreaSerializer

from area.exceptions import (
    AreaNotFound,
    ProviderAreaNotFound, 
    LatLongAreaNotFound,
    PolygonNotFound,
    QueryParamsWrong,
    QueryParamsProviderIdWrong
)
from shapely.geometry import Polygon, Point

class AreaService():

    def get(self):
        """
        A service for get all areas (polygons).
        """
        areas = Area.objects.all()

        return areas

    def create(self, serializer):
        """
        A service for create area (polygon).

        Args:

            serializer - serializer validated for save.

        Response:

            data - serializer data.
        """
        serializer.save()

        return serializer.data

    def update(self, validated_data, id):
        """
        A service for update area (polygon).

        Args:

            validated_data - serializer data validated.
            id - id of area. 

        Response:

            area - area object.
        """
        
        try:
            area = Area.objects.get(id=id)
        except Area.DoesNotExist as exp:
            raise AreaNotFound

        validated_data_dict = dict(validated_data.items())

        if "name" in validated_data_dict:
            area.name = validated_data_dict["name"]
        if "price" in validated_data_dict:
            area.price = validated_data_dict["price"]
        if "geojson" in validated_data_dict:
            area.geojson = validated_data_dict["geojson"]
        if "provider" in validated_data_dict:
            area.provider = validated_data_dict["provider"]
        
        area.save()

        return area

    def delete(self, id):
        """
        A service for delete area.

        Args:

            id - id of area. 
        """
        try:
            area = Area.objects.get(id=id)
        except Area.DoesNotExist as exp:
            raise AreaNotFound

        area.delete()

    def filter_by_provider(self, provider_id):
        """
        A service filter areas by provider id.

        Args:

            id - id of provider. 
        """
        if not provider_id:
            raise QueryParamsProviderIdWrong

        try:
            areas = Area.objects.filter(provider=provider_id)
        except Area.DoesNotExist as exp:
            raise ProviderAreaNotFound

        if not areas:
            raise ProviderAreaNotFound
        
        return areas

    def filter_by_coordinate(self, lat, long):
        """
        A service filter areas by coordinates.

        Args:

            lat - latitude choose by user.
            long - longitude choose by user. 
        """
        if not lat or not long:
            raise LatLongAreaNotFound

        try:
            point = Point(float(lat), float(long))
        except ValueError:
            raise QueryParamsWrong

        areas = Area.objects.all()
        
        areas_filter = []
        list_geojson = {}

        for area in areas:

            try:
                list_geojson = eval(area.geojson)
            except Exception as exp:
                pass

            if len(list_geojson) > 2:

                poly = Polygon(list_geojson)

                if poly.contains(point):
                    areas_filter.append(AreaSerializer(area).data)

        if not areas_filter:
            raise PolygonNotFound
        
        return areas_filter