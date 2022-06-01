"""
Bussines Logic

Author: Caio Henrique 
Email: caiocomputacao2014@gmail.com
"""

from provider.models import Provider
from provider.exceptions import ProviderNotFound

class ProviderService():

    def get_all(self):
        """
        A service for get all providers.
        """
        providers = Provider.objects.all()

        return providers

    def create(self, serializer):
        """
        A service for create provider.

        Args:

            serializer - serializer validated for save

        Response:

            data - serializer data
        """
        serializer.save()

        return serializer.data

    def update(self, validated_data, id):
        """
        A service for update provider.

        Args:

            validated_data - serializer data validated
            id - id of provider 

        Response:

            provider - provider object
        """
        
        try:
            provider = Provider.objects.get(id=id)
        except Provider.DoesNotExist as exp:
            raise ProviderNotFound

        validated_data_dict = dict(validated_data.items())

        if "name" in validated_data_dict:
            provider.name = validated_data_dict["name"]
        if "email" in validated_data_dict:
            provider.email = validated_data_dict["email"]
        if "phone" in validated_data_dict:
            provider.phone = validated_data_dict["phone"]
        if "language" in validated_data_dict:
            provider.language = validated_data_dict["language"]
        if "currency" in validated_data_dict:
            provider.currency = validated_data_dict["currency"]
        
        provider.save()

        return provider

            
