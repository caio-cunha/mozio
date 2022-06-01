from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework import status
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

    def post(self, request):
        """
        A view for create area (polygon).

        Args:
            request - Area request object.

        Returns:
            response - Provider created.
        """
        area_service = AreaService()
        serializer = AreaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        area = area_service.create(serializer=serializer)
        return Response(area, status=status.HTTP_201_CREATED)


class AreaViewDetail(APIView):
    pass