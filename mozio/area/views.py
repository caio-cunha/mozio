from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.pagination import LimitOffsetPagination
from area.services import AreaService
from area.serializers import AreaSerializer

class AreaView(APIView, LimitOffsetPagination):

    def get(self, request):
        """
        A view for get all area (polygon).

        Args:
            request - Area request object.

        Returns:
            response - All areas.
        """
        
        area_service = AreaService()
        areas = area_service.get()
        results = self.paginate_queryset(areas, request, view=self)
        serializer = AreaSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)

class AreaViewDetail(APIView):
    pass