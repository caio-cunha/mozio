"""
Bussines Logic

Author: Caio Henrique 
Email: caiocomputacao2014@gmail.com
"""

from provider.models import Provider

class ProviderService():

    def get_all(self):
        """
        A service for get all providers.
        """
        providers = Provider.objects.all()

        return providers

    def create(self, serializer):
        
        serializer.save()

        return serializer.data
