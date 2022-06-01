"""
Bussines Logic

Author: Caio Henrique 
Email: caiocomputacao2014@gmail.com
"""

from area.models import Area
from area.exceptions import AreaNotFound

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