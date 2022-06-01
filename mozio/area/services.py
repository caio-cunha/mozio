"""
Bussines Logic

Author: Caio Henrique 
Email: caiocomputacao2014@gmail.com
"""

from area.models import Area

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