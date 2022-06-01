from rest_framework.views import APIView
from rest_framework.response import Response
from provider.services import ProviderService
from provider.serializers import ProviderSerializer
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

class ProviderView(APIView, LimitOffsetPagination):

    permission_classes = (IsAuthenticated,)  

    def get(self, request):
        """
        A view for get all providers.

        Args:
            request - Provider request object.

        Returns:
            response - All providers.
        """
        
        provider_service = ProviderService()
        providers = provider_service.get_all()
        results = self.paginate_queryset(providers, request, view=self)
        serializer = ProviderSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request):
        """
        A view for create one provider.

        Args:
            request - Provider request object.

        Returns:
            response - Provider created.
        """

        provider_service = ProviderService()
        serializer = ProviderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        provider = provider_service.create(serializer=serializer)
        return Response(provider, status=status.HTTP_201_CREATED)


class ProviderViewDetail(APIView):

    permission_classes = (IsAuthenticated,)  
    
    def patch(self, request, id=None):
        """
        A view for update one provider.

        Args:
            request - Provider request object.
            id - Id for provider.

        Returns:
            response - Provider updated.
        """

        provider_service = ProviderService()
        serializer = ProviderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        provider = provider_service.update(validated_data=serializer.validated_data, id=id)
        return Response(ProviderSerializer(provider).data, status=status.HTTP_200_OK)

    def delete(self, id):
        """
        A view for delete one provider.

        Args:
            id - Id Provider.

        Returns:
            response - HTTP Status.
        """

        provider_service = ProviderService()
        provider_service.delete(id=id)
        return Response("", status=status.HTTP_204_NO_CONTENT)







