from rest_framework.views import APIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from area.services import AreaService
from area.serializers import AreaSerializer
from area.serializers import AreaPatchSerializer
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema

class AreaView(APIView, LimitOffsetPagination):

    permission_classes = (IsAuthenticated,)  

    @swagger_auto_schema(
        tags=["Area"],)
    def get(self, request):
        """
        A view for get all area (polygon).

        REQUEST_SERIALIZER \n
            {

            }

        RESPONSE_SERIALIZER \n
            {
                'count': 'count',
                'next': 'next',
                'previous': 'previous',
                'results': [
                    {
                        'id': 'id',
                        'name': 'name',
                        'price': 'price',
                        'provider': 'provider',
                        'geojson': 'geojson'
                    }
                ]
            }
        """
        
        area_service = AreaService()
        areas = area_service.get()
        results = self.paginate_queryset(areas, request, view=self)
        serializer = AreaSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)

    @swagger_auto_schema(
        tags=["Area"],request_body=AreaSerializer)
    def post(self, request):
        """
        A view for create area (polygon).

        REQUEST_SERIALIZER \n
            {
                'name': 'name',
                'price': 'price',
                'geojson': 'geojson',
                'provider': 'provider'
            }

        RESPONSE_SERIALIZER \n
            {
                'id': 'id',
                'name': 'name',
                'price': 'price',
                'provider': 'provider'
                'geojson': 'geojson'
            }
        """
        area_service = AreaService()
        serializer = AreaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        area = area_service.create(serializer=serializer)
        return Response(area, status=status.HTTP_201_CREATED)

class AreaViewDetail(APIView):

    permission_classes = (IsAuthenticated,)  
    
    @swagger_auto_schema(
        tags=["Area"],request_body=AreaPatchSerializer)
    def patch(self, request, id=None):
        """
        A view for update one area (polygon).

        REQUEST_SERIALIZER \n
            {
                'name': 'name',
                'price': 'price',
                'geojson': 'geojson',
                'provider': 'provider'
            }

        RESPONSE_SERIALIZER \n
            {
                'id': 'id',
                'name': 'name',
                'price': 'price',
                'provider': 'provider'
                'geojson': 'geojson'
            }
        """

        area_service = AreaService()
        serializer = AreaPatchSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        area = area_service.update(validated_data=serializer.validated_data, id=id)
        return Response(AreaPatchSerializer(area).data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        tags=["Area"],)
    def delete(self, request, id=None):
        """
        A view for delete one area (polygon).

        REQUEST_SERIALIZER \n
            {
            
            }

        RESPONSE_SERIALIZER \n
            {
                
            }
        """

        area_service = AreaService()
        area_service.delete(id=id)
        return Response("", status=status.HTTP_204_NO_CONTENT)

class AreaFilterView(APIView):

    permission_classes = (IsAuthenticated,)  

    def filter_by_provider(self):
        """
        A view for filter area (polygon) by provider.

        REQUEST_SERIALIZER \n
            {

            }

        RESPONSE_SERIALIZER \n
            [
                {                   
                    'id': 'id',
                    'name': 'name',
                    'price': 'price',
                    'provider': 'provider',
                    'geojson': 'geojson'
                }
            ]
        """
        provider_id = self.query_params.get('provider_id', None)
        area_service = AreaService()
        areas = area_service.filter_by_provider(provider_id)
        return Response(AreaSerializer(areas,many=True).data)

    @api_view(['GET'])
    def filter_by_cordinate(self):
        """
        A view for filter area (polygon) by coordinates.

        REQUEST_SERIALIZER \n
        {}

        RESPONSE_SERIALIZER \n
            [
                {                   
                    'id': 'id',
                    'name': 'name',
                    'price': 'price',
                    'provider': 'provider',
                    'geojson': 'geojson'
                }
            ]
        """
        lat = self.query_params.get('lat', None)
        long = self.query_params.get('long', None) 
        area_service = AreaService()
        areas = area_service.filter_by_coordinate(lat=lat, long=long)
        return Response(areas)