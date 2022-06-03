from rest_framework.views import APIView
from rest_framework.response import Response
from provider.services import ProviderService
from provider.serializers import ProviderSerializer
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema

class ProviderView(APIView, LimitOffsetPagination):

    permission_classes = (IsAuthenticated,)  

    def get(self, request):
        """
        A view for get all providers.

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
                        'email': 'email',
                        'phone': 'phone',
                        'language': 'language',
                        'currency','currency'
                    }
                ]
            }
        """
        
        provider_service = ProviderService()
        providers = provider_service.get_all()
        results = self.paginate_queryset(providers, request, view=self)
        serializer = ProviderSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)
    
    @swagger_auto_schema(
        request_body=ProviderSerializer)
    def post(self, request):
        """
        A view for create one provider.

        REQUEST_SERIALIZER \n
            {
                'name': 'name',
                'email': 'email',
                'phone': 'phone',
                'language': 'language',
                'currency','currency'
            }

        RESPONSE_SERIALIZER \n
            {
                'id': 'id',
                'name': 'name',
                'email': 'email',
                'phone': 'phone',
                'language': 'language',
                'currency','currency'
            }
        """

        provider_service = ProviderService()
        serializer = ProviderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        provider = provider_service.create(serializer=serializer)
        return Response(provider, status=status.HTTP_201_CREATED)


class ProviderViewDetail(APIView):

    permission_classes = (IsAuthenticated,)  
    
    @swagger_auto_schema(
        request_body=ProviderSerializer)
    def patch(self, request, id=None):
        """
        A view for update one provider.

        REQUEST_SERIALIZER \n
            {
                'name': 'name',
                'email': 'email',
                'phone': 'phone',
                'language': 'language',
                'currency','currency'
            }

        RESPONSE_SERIALIZER \n
            {
                'id': 'id',
                'name': 'name',
                'email': 'email',
                'phone': 'phone',
                'language': 'language',
                'currency','currency'
            }
        """

        provider_service = ProviderService()
        serializer = ProviderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        provider = provider_service.update(validated_data=serializer.validated_data, id=id)
        return Response(ProviderSerializer(provider).data, status=status.HTTP_200_OK)

    def delete(self, request, id=None):
        """
        A view for delete one provider.

        REQUEST_SERIALIZER \n
            {
            
            }

        RESPONSE_SERIALIZER \n
            {
                
            }
        """

        provider_service = ProviderService()
        print(id)
        provider_service.delete(id=id)
        return Response("", status=status.HTTP_204_NO_CONTENT)







