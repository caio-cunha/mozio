from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from provider.services import ProviderService
from provider.serializers import ProviderSerializer
from rest_framework.pagination import LimitOffsetPagination

class Provider(APIView, LimitOffsetPagination):
    """
        A class for CRUD provider
    """

    def get(self, request):
        """
        A view for get all providers

        Args:
            request - Provider request object.

        Returns:
            response - All providers
        """
        
        provider_service = ProviderService()
        providers = provider_service.get_all()
        results = self.paginate_queryset(providers, request, view=self)
        serializer = ProviderSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)


